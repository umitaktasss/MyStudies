#Verilen bir stringin kelime frekans�n� bulma

#Ad�m 1: K�t�phane ekleme Collestions

from collections import Counter

#Stringi tan�mla

text ="ThoroughbushthoroughbrierOverparkoverpale"

# Counter fonksiyonuyla frekans� bulabiliriz.

freq=Counter(text)

for letter, count in freq.items():
    print(f"'{letter} : {count}'")
    
freq2=Counter(text.lower())

print("----------------------Lower Case-----------------------------")
for letter, count in freq2.items():
    print(f"'{letter} : {count}'")