# gear/helpers.py
from typing import List
from .gear import Gear, Weapon, Chestplate  # Doğru sınıfları içe aktar

def equip_gear(gear: Gear):
    """
    Equips a Gear object and sets its is_equipped attribute to True.

    Args:
        gear (Gear): The Gear object to equip.
    """
    gear.set_equipped(True)

def unequip_gear(gear: Gear):
    """
    Unequips a Gear object and sets its is_equipped attribute to False.

    Args:
        gear (Gear): The Gear object to unequip.
    """
    gear.set_equipped(False)

def get_equipped_gear(all_gear: List[Gear]) -> List[Gear]:
    """
    Returns a list of all equipped Gear objects.

    Args:
        all_gear (List[Gear]): A list of all Gear instances.

    Returns:
        List[Gear]: A list of equipped Gear objects.
    """
    equipped_gear = [gear for gear in all_gear if gear.is_equipped]
    return equipped_gear

def print_equipped_gear(all_gear: List[Gear]):
    """
    Prints information about all equipped Gear objects.

    Args:
        all_gear (List[Gear]): A list of all Gear instances.
    """
    equipped_gear = get_equipped_gear(all_gear)
    if not equipped_gear:
        print("You have no equipped gear.")
        return

    print("**Equipped Gear:**")
    for gear in equipped_gear:
        print(f"- {gear.name}:")
        print(f"    Type: {gear.gear_type}")
        print(f"    Level: {gear.level}")
        print(f"    Rarity: {gear.rarity}")
        print(f"    Defense: {gear.defense}")
        print(f"    Durability: {gear.durability}")
        print(f"    Weight: {gear.weight}")
        if isinstance(gear, Chestplate):
            print(f"    Health Point: {gear.health_point}")
        if isinstance(gear, Weapon):
            print(f"    Attack: {gear.attack}")
        print()

    # Check for set bonus (assuming set IDs are unique)
    set_id = equipped_gear[0].id  # Assuming all equipped items have the same set ID
    if all(gear.id == set_id for gear in equipped_gear):
        bonus_multiplier = 2.0 if set_id == 1 else 2.5
        print(f"\n**Set Bonus (Set ID: {set_id})**")
        print(f"    Defense: x{bonus_multiplier}")
        print(f"    Durability: x{bonus_multiplier}")
        print(f"    Weight: x{bonus_multiplier}")
        print(f"    Health Point: x{bonus_multiplier} (if applicable)")
