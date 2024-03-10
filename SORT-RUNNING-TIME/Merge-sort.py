import time

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])


    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data[k] = left[i]
            i += 1
            k += 1
        else:
            data[k] = right[j]
            j += 1
            k += 1
            
    while i < len(left):
        data[k] = left[i]
        k += 1
        i += 1
        
    while j < len(right):
        data[k] = right[j]
        k += 1
        j += 1
        
    return data


for i in range(1, 11):
    with open(f"input{i}.txt", "r") as f:
         a = f.readline()  # Đọc dữ liệu 

    data = list(map(float, a.split())) 
    
    start_time = time.time()
    merge_sort(data)
    end_time = time.time()

    print(f"File input{i}.txt: {(end_time - start_time):.6f} giây")


