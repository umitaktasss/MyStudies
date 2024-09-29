max_weight = 15
# S�zl�kte sebze isimleriyle birlikte kilolar ve kar oranlar�
vegetables = {2: ("Tomato", 10), 3: ("Cucumber", 5), 5: ("Carrot", 15), 7: ("Pepper", 7), 1: ("Onion", 6), 4: ("Potato", 18), 1: ("Garlic", 3)}

# Kilogram ba��na kar oranlar�n� hesapla (kar/kg, kg, kar, sebze_ad�)
profit_per_kg = [(profit / kg, kg, profit, name) for kg, (name, profit) in vegetables.items()]

# Kar oranlar�na g�re s�ralama (en y�ksekten en d����e)
profit_per_kg.sort(reverse=True, key=lambda x: x[0])

total_profit = 0  # Total profit starts at 0
remaining_weight = max_weight

for profit_by_kg, kg, profit, name in profit_per_kg:  # Changed 'total_profit' to 'profit'
    if remaining_weight == 0:  # �uval doluysa break
        break

    # Ekleyebilece�imiz miktar mevcut a��rl�k veya sebzenin tamam� olabilir
    amount_to_take = min(kg, remaining_weight)

    total_profit += amount_to_take * profit_by_kg
    remaining_weight -= amount_to_take

    print(f"{amount_to_take} kg {name} has been added into the bag, The profit per kilogram: {profit_by_kg}, total profit={total_profit}")

print(f"The total profit made: {total_profit}")

    
