class Player:
    VERSION = "call always"

    def betRequest(self, game_state):
        print(game_state)
        print("got here")
        in_action = game_state['in_action']
        print(game_state["players"])
        us = game_state['players'][int(in_action)]
        print(us)
        all_cards = ["1","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        high_cards = ["A","K","Q","J","10"]

        hole1=us['hole_cards'][0]
        hole2=us['hole_cards'][1]

        match game_state["round"]:
            case 0: # Pre-flop
               print("Round one")
               if (hole1["rank"] == hole2["rank"]) or (hole1["suit"] == hole2["suit"] and abs(all_cards.index(hole1["rank"]) - all_cards.index(hole2["rank"])) == 1):
                   print("pocket pair or order suited")
                   return self.all_in(game_state)
               if hole1["rank"] in high_cards or hole2["rank"] in high_cards or (hole1["suit"] == hole2["suit"]) or  abs(all_cards.index(hole1["rank"]) - all_cards.index(hole2["rank"])) == 1:
                   print("high card or suited or ordered")
                   return self.bet(game_state)
               else:
                    print("neither")
                    return self.check()
            case 1: # Flop

                print("second round")
                print(game_state["community_cards"])
                print(hole1)
                print(hole2)
                hand = [ hole1, hole2, game_state["community_cards"] ]
                print(hand)
                return self.check()


                # Check if we have any pairs with the flop
                # community_cards = game_state.get('community_cards', [])
                # if len(community_cards) >= 3:
                #     # Count how many of our hole cards match the community cards
                #     matches = sum(1 for card in [hole1, hole2]
                #                 if any(card["rank"] == comm["rank"] for comm in community_cards))
                #     if matches >= 1:  # We have at least a pair
                #         return self.bet(game_state)
                # return self.match(game_state)
                #return 0



            case _:
                print("not first round calling")
                return self.match(game_state)

    @staticmethod
    def match(game_state):
        in_action = game_state['in_action']
        current_buy_in = game_state['current_buy_in']
        players = game_state['players']
        return current_buy_in - players[in_action]['bet']

    @staticmethod
    def bet(game_state, additional=0):
        in_action = game_state['in_action']
        current_buy_in = game_state['current_buy_in']
        players = game_state['players']
        minimum_raise = game_state["minimum_raise"]
        return current_buy_in - players[in_action]['bet'] + minimum_raise + additional

    @staticmethod
    def check():
        return 0

    @staticmethod
    def all_in(game_state):
        in_action = game_state['in_action']
        players = game_state['players']
        return players[in_action]['stack']

    def showdown(self, game_state):
        pass


def rank_poker_hand(hand):
    rank_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    ranks = sorted([rank_values[card['rank']] for card in hand], reverse=True)
    suits = [card['suit'] for card in hand]

    is_flush = len(set(suits)) == 1
    is_straight = ranks == list(range(ranks[0], ranks[0] - 5, -1))
    # Handle special case of low-Ace straight (A,2,3,4,5)
    if ranks == [14, 5, 4, 3, 2]:
        is_straight = True
        ranks = [5, 4, 3, 2, 1]

    from collections import Counter
    rank_counts = Counter(ranks)
    counts = sorted(rank_counts.values(), reverse=True)
    unique_ranks = sorted(rank_counts.keys(), reverse=True)

    if is_straight and is_flush and ranks[0] == 14:
        return "Royal Flush"
    elif is_straight and is_flush:
        return "Straight Flush"
    elif counts[0] == 4:
        return "Four of a Kind"
    elif counts[0] == 3 and counts[1] == 2:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "Straight"
    elif counts[0] == 3:
        return "Three of a Kind"
    elif counts[0] == 2 and counts[1] == 2:
        return "Two Pair"
    elif counts[0] == 2:
        return "One Pair"
    else:
        return "High Card"




