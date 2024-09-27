import heapq

def optimal_merge(files):
    # Min heap olu�turuyoruz
    heapq.heapify(files)
    
    total_cost = 0
    merge_steps = []  # Her birle�tirme ad�m�n� saklamak i�in bir liste
    
    # Heap'te 2 veya daha fazla eleman oldu�u s�rece devam et
    while len(files) > 1:
        # En k���k iki dosyay� al
        first = heapq.heappop(files)
        second = heapq.heappop(files)
        
        # Bu iki dosyay� birle�tir ve maliyeti hesapla
        merged_file = first + second
        total_cost += merged_file
        
        # Yeni dosyay� tekrar heap'e ekle
        heapq.heappush(files, merged_file)
        
        # Birle�tirme ad�m�n� kaydet
        merge_steps.append(f"Merged {first} and {second} into {merged_file} with cost {merged_file}")
    
    return total_cost, merge_steps

# �rnek dosya boyutlar�
files = [20, 30, 10, 5, 25]

# Optimal Merge Pattern ile minimum maliyet ve birle�tirme ad�mlar�
total_cost, merge_steps = optimal_merge(files)
print(f"Total minimum merge cost: {total_cost}")
for step in merge_steps:
    print(step)

