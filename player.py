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
