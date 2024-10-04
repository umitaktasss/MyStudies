#Verilen K�l��lar�n g��lerine g�re s�ralama
def sorted_power(Swords):
    Swords_Power={
                  "Saint George":100,
                  "King Arthur":95,
                  "Knight Killer":77,
                  "Dishonored Baron's Sword":85,
                  "Henchmen Sword":80
                  }
    sorted_Swords=sorted(Swords,key=lambda swords:Swords_Power[swords],reverse=True)
    return [(sword, Swords_Power[sword]) for sword in sorted_Swords]



Swords=["Saint George","King Arthur","Knight Killer","Dishonored Baron's Sword","Henchmen Sword"]
sorted_swords_list=sorted_power(Swords)
# K�l��lar� g��leriyle birlikte yazd�r
for sword, power in sorted_swords_list:
    print(f"{sword}: {power}")