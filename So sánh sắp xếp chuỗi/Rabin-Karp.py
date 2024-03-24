# ###Code GeekforGeeks
# # d is the number of characters in the input alphabet
# d = 256
# # pat -> pattern
# # text -> text
# # prime -> A prime number
# def search(pattern, text, prime):
# 	M = len(pattern)
# 	N = len(text)
# 	i = 0
# 	j = 0
# 	p = 0 # hash value for pattern
# 	t = 0 # hash value for text
# 	h = 1
# 	# The value of h would be "pow(d, M-1)%prime"
# 	for i in range(M-1):
# 		h = (h*d) % prime
  
# 	# Calculate the hash value of pattern and first window of text

# 	for i in range(M):
# 		p = (d*p + ord(pattern[i])) % prime
# 		t = (d*t + ord(text[i])) % prime
  
# 	# Slide the pattern over text one by one

# 	for i in range(N-M+1):
# 		# Check the hash values of current window of text and
# 		# pattern if the hash values match then only check
# 		# for characters one by one
# 		if p == t:
# 			# Check for characters one by one
# 			for j in range(M):
# 				if text[i+j] != pattern[j]:
# 					break
# 				else:
# 					j += 1

# 			# if p == t and pattern[0...M-1] = text[i, i+1, ...i+M-1]
# 			if j == M:
# 				print("patterntern found at index " + str(i))

# 		# Calculate hash value for next window of text: Remove
# 		# leading digit, add trailing digit
# 		if i < N-M:
# 			t = (d*(t-ord(text[i])*h) + ord(text[i+M])) % prime

# 			# We might get negative values of t, converting it to
# 			# positive
# 			if t < 0:
# 				t = t+prime

# if __name__ == '__main__':
# 	text = "GEEKS FOR GEEKS"
# 	pattern = "GEEK"
# 	# A prime number
# 	prime = 6469
# 	# Function Call
# 	search(pattern, text, prime)

def search(pattern, text, prime=6469):  # prime là số nguyên tố bất kì để dùng modulo, có thể chọn lớn hơn để tránh xung đột hơn nếu dữ liệu vào lớn hơn
    base = 256
    lp = len(pattern)
    lt = len(text)

    if lt < lp:
        return []  

    h = 1
    for _ in range(lp - 1):
        h = (h * base) % prime # Calculate h = (base^(m-1))%prime

    pattern_hash = 0
    text_hash = 0
 # Tính toán giá trị băm ban đầu cho pattern và text (chỉ tính trên lp ký tự đầu tiên của text).
    for i in range(lp):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    indices = []
#Khởi tạo một danh sách để lưu các chỉ số mà pattern đã xuất hiện trong text.
    for i in range(lt - lp + 1):#duyệt qua text từ đầu đến cuối, mỗi lần dịch chuyển một ký tự.
        if pattern_hash == text_hash:#nếu giá trị băm giống nhau,kiểm tra pattern và text.
            if text[i:i + lp] == pattern:
                indices.append(i) #nếu pattern giống text, thêm chỉ số vào danh sách.
 
 #Cập nhật giá trị băm của text để chuẩn bị cho lần lặp tiếp theo.
 #Điều này được thực hiện bằng cách loại bỏ ký tự đầu tiên và thêm ký tự tiếp theo vào giá trị băm.
        if i < lt - lp:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + lp])) % prime
#phép chia lấy dư có thể tạo ra số âm nên cần chuyển nó thành số dương.
            if text_hash < 0:
                text_hash += prime

    return indices


text = "ABABDABACDABABCABABABABCABAB"
pattern = "ABABCABAB"
occurrences = search(pattern, text)
print("Pattern found at index", occurrences)


