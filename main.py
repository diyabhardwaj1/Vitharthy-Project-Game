from player import Player
from rooms import create_rooms
from combat import battle
from utils import show_intro, get_choice


def main():
    show_intro()

    player = Player("Hero")
    rooms = create_rooms()

    current_room = "entrance"

    while player.is_alive():
        room = rooms[current_room]

        print("\n" + "=" * 50)
        print(f"You are in: {room['name']}")
        print(room["description"])

        # Show items in the room
        if room["items"]:
            print("\nItems here:")
            for item in room["items"]:
                print(f"- {item}")

        # Enemy encounter
        if room["enemy"] is not None:
            enemy = room["enemy"]

            print(f"\n⚔️ A {enemy['name']} appears!")

            won = battle(player, enemy)

            if not won:
                print("\nYou have been defeated.")
                print("GAME OVER!")
                return

            room["enemy"] = None

        # Get player choices
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Check inventory")
        print("3. Check health")
        print("4. Leave room")

        choice = get_choice(["1", "2", "3", "4"])

        if choice == "1":
            if room["items"]:
                item = room["items"].pop(0)
                player.add_item(item)
                print(f"\nYou picked up: {item}")
            else:
                print("\nYou search the room but find nothing useful.")

        elif choice == "2":
            player.show_inventory()

        elif choice == "3":
            print(f"\nHealth: {player.health}/{player.max_health}")

        elif choice == "4":
            if room["next_room"] is None:
                print("\n🎉 You found the exit!")
                print("Congratulations! You escaped the dungeon!")
                return

            current_room = room["next_room"]

    print("\nGAME OVER!")


if __name__ == "__main__":
    main()
