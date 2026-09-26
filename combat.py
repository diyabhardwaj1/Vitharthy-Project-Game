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
