# gear/create_set.py
from .gear import Weapon, Chestplate, Helmet, Boots, Shield

def create_dragon_slayer_set():
    return [
        Helmet(
            name="Dragon Slayer's Helmet", 
            gear_type="Helmet", 
            level=10,
            rarity="Epic", 
            defense=15, 
            durability=100.0,
            weight=5.0, 
            health_point=50,
            id=1  # Assign ID 1 for Dragon Slayer set
        ),
        Chestplate(
            name="Dragon Slayer's Chestplate", 
            gear_type="Chestplate", 
            level=10, 
            rarity="Epic", 
            defense=30, 
            durability=150.0,
            weight=10.0, 
            health_point=100,
            id=1  # Assign ID 1 for Dragon Slayer set
        ),
        Weapon(
            name="Dragon Slayer's Sword", 
            gear_type="Sword", 
            level=10, 
            rarity="Epic", 
            defense=0, 
            durability=200.0, 
            weight=7.0, 
            attack=50,
            id=1  # Assign ID 1 for Dragon Slayer set
        ),
        Boots(
            name="Dragon Slayer's Boots", 
            gear_type="Boots",
            level=10, 
            rarity="Epic", 
            defense=10, 
            durability=80.0, 
            weight=3.0, 
            health_point=20,
            id=1  # Assign ID 1 for Dragon Slayer set
        ),
        Shield(
            name="Dragon Slayer's Shield", 
            gear_type="Shield", 
            level=10, 
            rarity="Epic", 
            defense=40, 
            durability=250.0, 
            weight=12.0, 
            attack=0,
            id=1  # Assign ID 1 for Dragon Slayer set
        )
    ]

def create_phoenix_guard_set():
    return [
        Helmet(
            name="Phoenix Guard's Helmet",
            gear_type="Helmet",
            level=15,
            rarity="Epic",
            defense=20,
            durability=100.0,
            weight=2.0,
            health_point=50,
            id=2  # Assign ID 2 for Phoenix Guard set
        ),
        Chestplate(
            name="Phoenix Guard's Chestplate",
            gear_type="Chestplate",
            level=15,
            rarity="Epic",
            defense=40,
            durability=150.0,
            weight=8.0,
            health_point=120,
            id=2  # Assign ID 2 for Phoenix Guard set
        ),
        Weapon(
            name="Phoenix Guard's Spear",
            gear_type="Spear",
            level=15,
            rarity="Epic",
            defense=0,
            durability=120.0,
            weight=5.0,
            attack=60,
            id=2  # Assign ID 2 for Phoenix Guard set
        ),
        Boots(
            name="Phoenix Guard's Boots",
            gear_type="Boots",
            level=15,
            rarity="Epic",
            defense=10,
            durability=80.0,
            weight=1.5,
            health_point=30,
            id=2  # Assign ID 2 for Phoenix Guard set
        ),
        Shield(
            name="Phoenix Guard's Shield",
            gear_type="Shield",
            level=15,
            rarity="Epic",
            defense=50,
            durability=200.0,
            weight=6.0,
            attack=0,
            id=2  # Assign ID 2 for Phoenix Guard set
        )
    ]
