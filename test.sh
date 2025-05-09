curl -d 'action=bet_request&game_state={

    "tournament_id":"550d1d68cd7bd10003000003",

    "game_id":"550da1cb2d909006e90004b1",

    "round":1,

    "bet_index":0,

    "small_blind": 10,

    "current_buy_in": 320,

    "pot": 400,

    "minimum_raise": 240,

    "dealer": 1,

    "orbits": 7,

    "in_action": 1,

    "players": [
        {

            "id": 0,

            "name": "Albert",

            "status": "active",

            "version": "Default random player",

            "stack": 1010,

            "bet": 320
        },
        {

            "id": 1,
            "name": "Bob",
            "status": "active",
            "version": "Default random player",
            "stack": 1590,
            "bet": 80,

            "hole_cards": [
                {

                    "rank": "3",

                    "suit": "hearts"                },
                {
                    "rank": "K",
                    "suit": "hearts"
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

    "community_cards": [
                {

                    "rank": "3",

                    "suit": "hearts"                },
                {
                    "rank": "K",
                    "suit": "hearts"
                }
    ]
}
' localhost:9000
