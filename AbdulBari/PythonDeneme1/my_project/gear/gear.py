# gear/gear.py
class Gear:
    def __init__(self, name: str, gear_type: str, level: int, rarity: str, defense: int, durability: float, weight: float, id: int):
        self.name = name
        self.gear_type = gear_type
        self.level = level
        self.rarity = rarity
        self.defense = defense
        self.durability = durability
        self.weight = weight
        self.id = id
        self.is_equipped = False
        self.health_point = 0  # Initialize HealthPoint attribute

    def set_equipped(self, value: bool):
        self.is_equipped = value

    def double_up_stats(self, equipped_gear: list):
        """
        Doubles up stats if all equipped items have the same set ID.

        Args:
            equipped_gear (list[Gear]): A list of equipped Gear objects.
        """
        if not equipped_gear:  # Handle empty equipped_gear list
            return

        set_id = equipped_gear[0].id
        if all(gear.id == set_id for gear in equipped_gear):
            multiplier = 2.0 if set_id == 1 else 2.5  # Set-specific multipliers
            self.defense *= multiplier
            self.durability *= multiplier
            self.weight *= multiplier
            self.health_point *= multiplier

class Weapon(Gear):
    def __init__(self, name: str, gear_type: str, level: int, rarity: str, defense: int, durability: float, weight: float, id: int, attack: int):
        super().__init__(name, gear_type, level, rarity, defense, durability, weight, id)
        self.attack = attack

class Chestplate(Gear):
    def __init__(self, name: str, gear_type: str, level: int, rarity: str, defense: int, durability: float, weight: float, id: int, health_point=0):
        super().__init__(name, gear_type, level, rarity, defense, durability, weight, id)
        self.health_point = health_point

class Helmet(Chestplate):
    pass

class Boots(Chestplate):
    pass

class Shield(Weapon):
    pass
