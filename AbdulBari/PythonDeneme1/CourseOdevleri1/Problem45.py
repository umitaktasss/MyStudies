#Gmail format�nda olan eposta adreslerini tan�mlayan bir d�zenli ifade yazmak i�in
import re
#Bo� bir liste emailleri tutmak i�in
gmail_emails = []
gmail_pattern =  r"[a-zA-Z0-9._%+-]+@gmail\.com$"


file_path=r"C:\Users\Tulpar\Desktop\Algorithm\PythonDeneme1\PythonDeneme1\CourseOdevleri1\Text\mailler.txt"

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()  # Sat�r sonundaki bo�luklar� ve \n karakterini temizle
        if re.match(gmail_pattern, line):  # Gmail format�na uygun olup olmad���n� kontrol et
            gmail_emails.append(line)  # Uyanlar� listeye ekle
print("Gmail Adresleri:")
for email in gmail_emails:
    print(email)