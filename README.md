# Vitharthy-Project-Game
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
class Player:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.health = 100
        self.attack_power = 15
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

        if self.health < 0:
            self.health = 0

        print(f"{self.name} takes {damage} damage!")
        print(f"Health: {self.health}/{self.max_health}")

    def heal(self, amount):
        self.health += amount

        if self.health > self.max_health:
            self.health = self.max_health

        print(f"You healed for {amount} health.")
        print(f"Health: {self.health}/{self.max_health}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

        # Special item effects
        if item == "Magic Sword":
            self.attack_power += 10
            print("Your attack power increased!")

        elif item == "Health Potion":
            self.heal(30)

    def show_inventory(self):
        print("\n--- INVENTORY ---")

        if not self.inventory:
            print("Your inventory is empty.")
        else:
            for item in self.inventory:
                print(f"- {item}")
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
import random


def battle(player, enemy):

    enemy_health = enemy["health"]

    print("\n==============================")
    print(f"BATTLE: {enemy['name']}")
    print("==============================")

    while enemy_health > 0 and player.is_alive():

        print("\nChoose your action:")
        print("1. Attack")
        print("2. Heal")

        choice = input("Enter your choice: ")

        if choice == "1":

            # Player attacks
            damage = random.randint(
                player.attack_power - 5,
                player.attack_power + 5
            )

            if damage < 1:
                damage = 1

            enemy_health -= damage

            print(f"\n⚔️ You attack the {enemy['name']}!")
            print(f"You deal {damage} damage.")

            if enemy_health <= 0:
                print(f"\n🎉 You defeated the {enemy['name']}!")
                return True

            print(f"{enemy['name']} health: {enemy_health}")

            # Enemy attacks
            enemy_damage = random.randint(
                enemy["attack"] - 3,
                enemy["attack"] + 3
            )

            player.take_damage(enemy_damage)

        elif choice == "2":

            if "Health Potion" in player.inventory:
                player.inventory.remove("Health Potion")
                player.heal(30)
            else:
                print("\nYou don't have a Health Potion!")

        else:
            print("\nInvalid choice.")

    return player.is_alive()
def show_intro():

    print("""
========================================
       ESCAPE THE DUNGEON
========================================

You wake up in a mysterious dungeon.

You don't remember how you got here.

Your goal is simple:

    ESCAPE THE DUNGEON!

Explore the rooms.
Collect useful items.
Fight enemies.
Find the exit.

Good luck, adventurer!
========================================
""")


def get_choice(valid_choices):

    while True:

        choice = input("\nEnter your choice: ").strip()

        if choice in valid_choices:
            return choice

        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
