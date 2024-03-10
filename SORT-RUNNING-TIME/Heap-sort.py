import time

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Xây dựng max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Sắp xếp mảng
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


    # Thống kê thời gian sắp xếp
for i in range(1, 11):
    with open(f"input{i}.txt", "r") as file:
        data = list(map(float, file.readline().strip().split()))  # Đọc dữ liệu và chuyển đổi sang list các số

    start_time = time.time()
    heap_sort(data)
    end_time = time.time()

    print(f"File input{i}.txt: {(end_time - start_time):.6f} giây")


