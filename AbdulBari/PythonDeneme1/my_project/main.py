# main.py
from gear import create_dragon_slayer_set, create_phoenix_guard_set, equip_gear, print_equipped_gear

# Global list of all gear
all_gear = []

# Dragon Slayer's Armament
dragon_slayer_set = create_dragon_slayer_set()
all_gear.extend(dragon_slayer_set)  # Add Dragon Slayer set to the global list

# Phoenix Guard's Regalia
phoenix_guard_set = create_phoenix_guard_set()
all_gear.extend(phoenix_guard_set)  # Add Phoenix Guard set to the global list

# Equip all Dragon Slayer gear
for gear in dragon_slayer_set:
    equip_gear(gear)

# Print equipped Dragon Slayer gear
print("Dragon Slayer's Armament:")
print_equipped_gear(all_gear)

# Equip all Phoenix Guard gear (optional)
for gear in phoenix_guard_set:
    equip_gear(gear)

# Print equipped Phoenix Guard gear
print("Phoenix Guard's Regalia:")
print_equipped_gear(all_gear)

