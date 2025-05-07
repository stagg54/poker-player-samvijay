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

        if game_state["community_cards"] == []:
           print("Preflop")
           if (hole1["rank"] == hole2["rank"]) or (hole1["suit"] == hole2["suit"] and abs(all_cards.index(hole1["rank"]) - all_cards.index(hole2["rank"])) == 1):
               print("pocket pair or order suited")
               return self.all_in(game_state)
           if hole1["rank"] in high_cards or hole2["rank"] in high_cards or (hole1["suit"] == hole2["suit"]) or  abs(all_cards.index(hole1["rank"]) - all_cards.index(hole2["rank"])) == 1:
               print("high card or suited or ordered")
               return self.bet(game_state)
           else:
               print("neither")
               return self.check()
        else: # Flop +

            print("post_flop")
            print(game_state["community_cards"])
            print(hole1)
            print(hole2)
            hand = [ hole1, hole2, game_state["community_cards"] ]
            print(hand)
            ( result, _) = best_poker_hand(us['hole_cards'],game_state['community_cards'])
            rank = result[0]
                #match rank:
                # SamVijay was disqualified for making an error: Failed to parse players response as non negative integer. Response was:
            if rank >= 7: #Full house or better
                return self.all_in(game_state)
            elif rank >= 3: #Two pair
                return self.bet(250)
            elif rank >= 2:  # One pair or better
                return self.bet(100) # check for high pair
            else:
                return self.check()


                #hand_rank, best_hand = best_poker_hand(us['hole_cards'], game_state['community_cards'])
                #print(f"Best hand rank: {hand_rank}")
                #print(f"Best hand: {best_hand}")

                # Get hand rank and cards

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
        return min(Player.all_in(game_state), current_buy_in - players[in_action]['bet'] + minimum_raise + additional)

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


import itertools
from collections import Counter


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
    # Handle low-Ace straight
    if ranks == [14, 5, 4, 3, 2]:
        is_straight = True
        ranks = [5, 4, 3, 2, 1]

    rank_counts = Counter(ranks)
    counts = sorted(rank_counts.values(), reverse=True)
    unique_ranks = sorted(rank_counts.keys(), reverse=True)

    # Assign a ranking tuple (higher is better)
    if is_straight and is_flush and ranks[0] == 14:
        return (10, ranks)  # Royal Flush
    elif is_straight and is_flush:
        return (9, ranks)  # Straight Flush
    elif counts[0] == 4:
        return (8, unique_ranks)  # Four of a Kind
    elif counts[0] == 3 and counts[1] == 2:
        return (7, unique_ranks)  # Full House
    elif is_flush:
        return (6, ranks)  # Flush
    elif is_straight:
        return (5, ranks)  # Straight
    elif counts[0] == 3:
        return (4, unique_ranks)  # Three of a Kind
    elif counts[0] == 2 and counts[1] == 2:
        return (3, unique_ranks)  # Two Pair
    elif counts[0] == 2:
        return (2, unique_ranks)  # One Pair
    else:
        return (1, ranks)  # High Card


def best_poker_hand(hole_cards, community_cards):
    all_cards = hole_cards + community_cards
    best_rank = (0, [])
    best_hand = None

    for combo in itertools.combinations(all_cards, 5):
        # Ensure at least one hole card is included
        if not any(card in hole_cards for card in combo):
            continue
        current_rank = rank_poker_hand(combo)
        if current_rank > best_rank:
            best_rank = current_rank
            best_hand = combo

    return best_rank, best_hand








