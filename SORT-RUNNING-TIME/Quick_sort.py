import random
import time

def partition(arr, low, high):
    pivot = random.randint(low, high)  # Chọn một pivot ngẫu nhiên
    pivot_index = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]  # Di chuyển pivot vào cuối mảng
    i = low - 1
    
    
    for j in range(low, high):
        if arr[j] <= pivot_index:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Để pivot lại chỗ giữa 2 phần nhỏ hơn và lớn hơn
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def main():
    # Thống kê thời gian sắp xếp
    for i in range(1, 11):
        with open(f"input{i}.txt", "r") as file:
            data = list(map(float, file.readline().strip().split()))  # Đọc dữ liệu và chuyển đổi sang list các số

        start_time = time.time()
        quick_sort(data, 0, len(data) - 1)
        end_time = time.time()

        print(f"File input{i}.txt: {(end_time - start_time):.6f} giây")

if __name__ == "__main__":
    main()
