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
