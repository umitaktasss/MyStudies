# Alfabetik s�ra dictionary'sini olu�tur
alphabet_dict = {chr(i): i - 64 for i in range(65, 91)}

# �simler.txt dosyas�n� oku
with open('isimler.txt', 'r') as file:
    names = file.read().replace('"', '').split(',')

# �simleri alfabetik olarak s�rala
names = [name.strip().upper() for name in names]
names.sort()

total_score = 0
print(f"Toplam isim: {len(names)}")
# Her ismin puan�n� hesapla
for index, name in enumerate(names):
    name_value = sum(alphabet_dict[char] for char in name if char in alphabet_dict)
    name_score = name_value * (index + 1)
    total_score += name_score

print(f"Tum isimlerin toplam puani: {total_score}")
#Yanl�� cevap ��z�lemedi
