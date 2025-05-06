class Player:
    VERSION = "strategy 2"

    def betRequest(self, game_state):
        print(game_state)
        print("got here")
        in_action = game_state['in_action']
        print(game_state["players"])
        us = game_state['players'][int(in_action)]
        print(us)
        high_cards = ["A","K","Q","J","10"]
        hole1=us['hole_cards'][0]
        hole2=us['hole_cards'][1]

        match game_state["round"]:
            case 0:
               print("Round one")
               if hole1["rank"] == hole2["rank"]:
                   print("pocket pair")
                   return self.all_in(game_state)
               if hole1["rank"] in high_cards or hole2["rank"] in high_cards:
                   print("high card")
                   return self.bet(game_state)
               else:
                    print("neither")
                    return self.check()
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

