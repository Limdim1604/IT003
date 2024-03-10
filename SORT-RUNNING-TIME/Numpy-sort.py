import numpy as np
import time

for i in range(1, 11):
    # Tạo tên tệp tin
    filename = "input" + str(i) + ".txt"
    # Đọc dữ liệu từ tệp tin vào mảng numpy
    data = np.loadtxt(filename)
    # Đo thời gian sắp xếp
    start_time = time.time()
    np.sort(data)
    end_time = time.time()
    # Tính thời gian sắp xếp
    duration = end_time - start_time
    # In thời gian sắp xếp
    print(f"Thời gian sắp xếp của tệp tin {filename}: {duration} giây.")
