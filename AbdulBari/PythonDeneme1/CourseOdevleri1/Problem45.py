#Gmail formatýnda olan eposta adreslerini tanýmlayan bir düzenli ifade yazmak için
import re
#Boþ bir liste emailleri tutmak için
gmail_emails = []
gmail_pattern =  r"[a-zA-Z0-9._%+-]+@gmail\.com$"


file_path=r"C:\Users\Tulpar\Desktop\Algorithm\PythonDeneme1\PythonDeneme1\CourseOdevleri1\Text\mailler.txt"

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()  # Satýr sonundaki boþluklarý ve \n karakterini temizle
        if re.match(gmail_pattern, line):  # Gmail formatýna uygun olup olmadýðýný kontrol et
            gmail_emails.append(line)  # Uyanlarý listeye ekle
print("Gmail Adresleri:")
for email in gmail_emails:
    print(email)