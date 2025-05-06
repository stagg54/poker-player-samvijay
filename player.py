class Player:
    VERSION = "call every time"

    def betRequest(self, game_state):
        in_action=game_state['in_action']
        current_buy_in=game_state['current_buy_in']
        players=game_state['players']

        return current_buy_in - players[in_action]['bet']

    @staticmethod
    def raise(game_state, additional=0):
        in_action = game_state['in_action']
        current_buy_in = game_state['current_buy_in']
        players = game_state['players']
        minimum_raise = game_state['minimum_raise']
        return current_buy_in - players[in_action]['bet'] + minimum_raise + additional

    def showdown(self, game_state):
        pass

