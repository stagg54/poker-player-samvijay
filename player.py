class Player:
    VERSION = "all in on pocket pair, bet on high card"

    def betRequest(self, game_state):
        in_action = game_state['in_action']
        us = game_state['players'][in_action]
        high_cards = ["A","K","Q","J","10"]
        if game_state['round'] == 0:
            if us["hole_cards"]["rank"][0] == us["hole_cards"]["rank"][1]:
                return self.all_in(game_state)
            if us["hole_cards"]["rank"][0] in high_cards or us["hole_cards"]["rank"][1] in high_cards:
                return self.bet(game_state)
            else:
                return self.check()
        else:
            return self.call(game_state)

    @staticmethod
    def call(game_state):
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

