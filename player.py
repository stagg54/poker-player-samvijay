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


def rank(hand):
