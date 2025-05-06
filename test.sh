curl -d 'action=bet_request&game_state={
    // Id of the current tournament
    "tournament_id":"550d1d68cd7bd10003000003",

    // Id of the current sit'n'go game. You can use this to link a
    // sequence of game states together for logging purposes, or to
    // make sure that the same strategy is played for an entire game
    "game_id":"550da1cb2d909006e90004b1",

    // Index of the current round within a sit'n'go
    "round":0,

    // Index of the betting opportunity within a round
    "bet_index":0,

    // The small blind in the current round. The big blind is twice
    // the small blind
    "small_blind": 10,

    // The amount of the largest current bet from any one player
    "current_buy_in": 320,

    // The size of the pot (sum of the player bets)
    "pot": 400,

    // Minimum raise amount. To raise you have to return at least:
    // current_buy_in - players[in_action][bet] + minimum_raise
    "minimum_raise": 240,

    // The index of the player on the dealer button in this round
    // The first player is (dealer+1)%(players.length)
    "dealer": 1,

    // Number of orbits completed. (The number of times the dealer
    //     button returned to the same player.)
    "orbits": 7,

    // The index of your player, in the players array
    "in_action": 1,

    // An array of the players. The order stays the same during the
    //     entire tournament
    "players": [
        {
            // Id of the player (same as the index)
            "id": 0,

            // Name specified in the tournament config
            "name": "Albert",

            // Status of the player:
            //   - active: the player can make bets, and win
            //     the current pot
            //   - folded: the player folded, and gave up interest in
            //     the current pot. They can return in the next round.
            //   - out: the player lost all chips, and is out of this
            //     sit'n'go
            "status": "active",

            // Version identifier returned by the player
            "version": "Default random player",

            // Amount of chips still available for the player.
            // (Not including the chips the player bet in
            // this round.)
            "stack": 1010,

            // The amount of chips the player put into the pot
            "bet": 320
        },
        {
            // Your own player looks similar, with one extension.
            "id": 1,
            "name": "Bob",
            "status": "active",
            "version": "Default random player",
            "stack": 1590,
            "bet": 80,
            // The cards of the player. This is only visible for
            // your own player except after showdown, when cards
            // revealed are also included.
            "hole_cards": [
                {
                    // Rank of the card. Possible values are
                    // numbers 2-10 and J,Q,K,A
                    "rank": "6",
                    // Suit of the card. Possible values are:
                    // clubs,spades,hearts,diamonds
                    "suit": "hearts"
                },
                {
                    "rank": "K",
                    "suit": "spades"
                }
            ]
        },
        {
            "id": 2,
            "name": "Chuck",
            "status": "out",
            "version": "Default random player",
            "stack": 0,
            "bet": 0
        }
    ],
    // Finally the array of community cards.
    "community_cards": [
        {
            "rank": "4",
            "suit": "spades"
        },
        {
            "rank": "A",
            "suit": "hearts"
        },
        {
            "rank": "6",
            "suit": "clubs"
        }
    ]
}
' localhost:9000
