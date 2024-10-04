from pyexpat import model
import random

class Sword():
    def __init__(self, model, damage, durability, extra1, extra2):
        self.model = model
        self.damage = damage
        self.durability = durability
        self.extra1 = extra1
        self.extra2 = extra2
        
    def bilgilerigoster(self):
        print("""              *******************
              Model: {}
              Damage: {}
              Durabilitiy: {}
              extra1: {}
              extra2: {}
              *******************""".format(self.model,self.damage,self.durability,self.extra1,self.extra2))

WoodenSword = Sword("Common", random.randint(1, 5), 10, "null", "null")
Baron_Sword = Sword("Rare", random.randint(25, 35), 50, "Nobility +50", "null")
St_George_Sword = Sword("Legendary", random.randint(50, 75), 100, "%50 extra damage against unholly creatures", "Holiness +100")
WoodenSword.bilgilerigoster()
Baron_Sword.bilgilerigoster()
St_George_Sword.bilgilerigoster()
