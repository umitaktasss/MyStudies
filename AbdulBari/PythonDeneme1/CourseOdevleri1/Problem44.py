#Dosya yolu belirleme
file_path=r"C:\Users\Tulpar\Desktop\Algorithm\PythonDeneme1\PythonDeneme1\CourseOdevleri1\Text\Poem.txt"

initials=""
with open(file_path, 'r') as file:
    for line in file:
        line= line.strip() #sat�r sonlardaki bo�luklar temizlenir.
        if len(line) >0:
            initials += line[0]
    
print(f"The initials are: '{initials}'")
