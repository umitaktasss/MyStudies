class Sword:
    def __init__(self, Power: int, Type: str, Faith: str, Grip: str, Legend: str):
        self.Power = Power
        self.Type = Type
        self.Faith = Faith
        self.Grip = Grip
        self.Legend = Legend

    
    def sort_swords(swords):
        sorted_swords = sorted(swords, key=lambda sword: sword.Power, reverse=True)
        return sorted_swords
    def sort_swords_Faith(swords):
        faith_order = {'Holy': 0, 'Unholy': 1}
        sorted_swords_faith = sorted(swords, key=lambda sword: faith_order[sword.Faith])
        return sorted_swords_faith

       

            

#Legendary
saint_George = Sword(100, "Legendary", "Holy", "Two-Handed-Sword", "Church")
Durendal = Sword(90,"Legendary","Holy","One-Handed-Sword","French")
Gram = Sword(95, "Legendary", "Holy", "One-Handed Sword", "Norse")
Joyeuse = Sword(90, "Legendary", "Holy", "One-Handed Sword", "French")
Zulfiqar = Sword(85, "Legendary", "Holy", "Two-Handed Sword", "Islamic")
Tizona = Sword(80, "Legendary", "Holy", "One-Handed Sword", "Spanish")
Clarent = Sword(75, "Legendary", "Holy", "One-Handed Sword", "Arthurian")
Excalibur = Sword(100, "Legendary", "Holy", "Two-Handed Sword", "Arthurian")

# Rare Swords (Power: 50-60)
preacher=Sword(60,"Rare","Holy","One-Handed-Sword","Church")
Dragonbane = Sword(60, "Rare", "Holy", "One-Handed Sword", "French")
Sunblade = Sword(55, "Rare", "Holy", "One-Handed Sword", "Norse")
Soulreaper = Sword(50, "Rare", "Holy", "Two-Handed Sword", "Islamic")
# Uncommon Swords (Power: 45-50)
Silverlight = Sword(50, "Uncommon", "Holy", "One-Handed Sword", "Arthurian")
Shadowstrike = Sword(48, "Uncommon", "Holy", "Dagger", "Spanish")
Frostbite = Sword(45, "Uncommon", "Holy", "One-Handed Sword", "French")
# Common Swords (Power: 30-45)
Ironblade = Sword(45, "Common", "Holy", "One-Handed Sword", "Norse")  
Oakenshield = Sword(40, "Common", "Holy", "One-Handed Sword", "Arthurian")  
Rustyblade = Sword(35, "Common", "Holy", "One-Handed Sword", "Spanish")

# Legendary Unholy Swords (Power: 75-100)
Doombringer = Sword(100, "Legendary", "Unholy", "Two-Handed Sword", "Cult of Darkness")
Soulharvester = Sword(90, "Legendary", "Unholy", "One-Handed Sword", "Demonic Legion")
Ebonrazor = Sword(85, "Legendary", "Unholy", "One-Handed Sword", "Shadow Council")
# Rare Unholy Swords (Power: 50-60)
Shadowfang = Sword(60, "Rare", "Unholy", "One-Handed Sword", "Dark Cult")
Demoniccleaver = Sword(55, "Rare", "Unholy", "Two-Handed Sword", "Demon Realm")
Soulreaper = Sword(50, "Rare", "Unholy", "One-Handed Sword", "Cultist")
# Uncommon Unholy Swords (Power: 45-50)
Bloodthirst = Sword(50, "Uncommon", "Unholy", "Dagger", "Vampire Coven")
Necroticblade = Sword(48, "Uncommon", "Unholy", "One-Handed Sword", "Necromancer")
Cursedscimitar = Sword(45, "Uncommon", "Unholy", "One-Handed Sword", "Haunted Tomb")
# Common Unholy Swords (Power: 30-45)
Fellblade = Sword(45, "Common", "Unholy", "One-Handed Sword", "Dark Cult")
Dreadscythe = Sword(40, "Common", "Unholy", "Two-Handed Sword", "Grim Reaper Cult")
Tainteddagger = Sword(35, "Common", "Unholy", "Dagger", "Occultist")

all_swords = [saint_George, Durendal, Gram, Joyeuse, Zulfiqar, Tizona, Clarent, Excalibur,
              preacher, Dragonbane, Sunblade, Soulreaper, Silverlight, Shadowstrike, Frostbite,
              Ironblade, Oakenshield, Rustyblade, Doombringer, Soulharvester, Ebonrazor,
              Shadowfang, Demoniccleaver, Bloodthirst, Necroticblade, Cursedscimitar,
              Fellblade, Dreadscythe, Tainteddagger]

# Sort the swords by power level in descending order
sorted_swords_by_power = Sword.sort_swords(all_swords)
sorted_swords_by_faith = Sword.sort_swords_Faith(all_swords)

# Print the sorted swords
for sword in sorted_swords_by_power:
    print(f"Power: {sword.Power}, Type: {sword.Type}, Faith: {sword.Faith}, Grip: {sword.Grip}, Legend: {sword.Legend}")
print("")
for sword in sorted_swords_by_faith:
    print(f"Power: {sword.Power}, Type: {sword.Type}, Faith: {sword.Faith}, Grip: {sword.Grip}, Legend: {sword.Legend}")
    
