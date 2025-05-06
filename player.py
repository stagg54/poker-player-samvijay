class Player:
    VERSION = "call every time"

    def betRequest(self, game_state):
        return self.call(game_state)

    @staticmethod
    def call(game_state):
        in_action = game_state['in_action']
        current_buy_in = game_state['current_buy_in']
        players = game_state['players']
        return current_buy_in - players[in_action]['bet']

    def showdown(self, game_state):
        pass

