def create_rooms():

    rooms = {
        "entrance": {
            "name": "Dungeon Entrance",
            "description": (
                "You wake up inside a dark dungeon. "
                "A strange passage leads deeper into the dungeon."
            ),
            "items": ["Health Potion"],
            "enemy": None,
            "next_room": "hall"
        },

        "hall": {
            "name": "Dark Hall",
            "description": (
                "The hall is covered with ancient paintings. "
                "You hear something moving in the darkness."
            ),
            "items": ["Magic Sword"],
            "enemy": {
                "name": "Goblin",
                "health": 50,
                "attack": 10
            },
            "next_room": "treasure"
        },

        "treasure": {
            "name": "Treasure Room",
            "description": (
                "You enter a room filled with old treasure. "
                "There is a huge door on the other side."
            ),
            "items": ["Gold Coin"],
            "enemy": {
                "name": "Dungeon Guard",
                "health": 70,
                "attack": 12
            },
            "next_room": "exit"
        },

        "exit": {
            "name": "Dungeon Exit",
            "description": (
                "A large stone door stands before you. "
                "You can finally escape the dungeon."
            ),
            "items": [],
            "enemy": None,
            "next_room": None
        }
    }

    return rooms
