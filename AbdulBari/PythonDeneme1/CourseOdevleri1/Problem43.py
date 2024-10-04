#Verilen bir stringin kelime frekansýný bulma

#Adým 1: Kütüphane ekleme Collestions

from collections import Counter

#Stringi tanýmla

text ="ThoroughbushthoroughbrierOverparkoverpale"

# Counter fonksiyonuyla frekansý bulabiliriz.

freq=Counter(text)

for letter, count in freq.items():
    print(f"'{letter} : {count}'")
    
freq2=Counter(text.lower())

print("----------------------Lower Case-----------------------------")
for letter, count in freq2.items():
    print(f"'{letter} : {count}'")