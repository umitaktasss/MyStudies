#Verilen Kýlýçlarýn güçlerine göre sýralama
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
# Kýlýçlarý güçleriyle birlikte yazdýr
for sword, power in sorted_swords_list:
    print(f"{sword}: {power}")