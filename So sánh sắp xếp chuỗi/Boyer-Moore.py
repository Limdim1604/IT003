# base = 256
# #Hàm dưới tạo ra một mảng Bad Character Heuristic được sử dụng trong thuật toán Boyer-Moore.
# def badCharHeuristic(string, size):
#     '''
#     The preprocessing function for
#     Boyer Moore's bad character heuristic
#     '''
#     #Khởi tạo mảng badChar all = -1. Mảng này sẽ lưu vị trí xuất hiện cuối cùng của mỗi ký tự trong chuỗi.
#     badChar = [-1]*base

#     # Điền vào mảng badChar vị trí xuất hiện cuối cùng của mỗi ký tự trong chuỗi.
#     for i in range(size):
#         badChar[ord(string[i])] = i

#     # return initialized list
#     return badChar

# #Hàm dưới tìm kiếm chuỗi sử dụng thuật toán Boyer-Moore
# def search(text, pattern):
#     '''
#     A pattern searching function that uses Bad Character
#     Heuristic of Boyer Moore Algorithm
#     '''
#     lp = len(pattern)
#     lt = len(text)
#     indices = []
#     # create the bad character list by calling
#     # the preprocessing function badCharHeuristic()
#     # for given pattern
#     badChar = badCharHeuristic(pattern, lp)

#     #s is shift of the pattern with respect to text
#     #Khởi tạo giá trị dịch chuyển s của chuỗi mẫu so với chuỗi văn bản.
#     s = 0
#     while(s <= lt-lp):
#         j = lp-1#Vòng lặp chính của thuật toán.Nếu chuỗi mẫu chưa dịch qua phải hết chuỗi văn bản, thì tiếp tục lặp.

#         # Keep reducing index j of pattern while
#         # characters of pattern and text are matching
#         # at this shift s
#         while j >= 0 and pattern[j] == text[s+j]:
#             j -= 1 
#         #Giảm chỉ số j của chuỗi mẫu khi các ký tự của chuỗi mẫu và chuỗi văn bản khớp nhau tại dịch chuyển hiện tại s.
#         # If the pattern is present at current shift,
#         # then index j will become -1 after the above loop
#         if j < 0:#Nếu chuỗi mẫu xuất hiện tại dịch chuyển hiện tại thì indices.append(s) 
#             #print("cur at shift = {}".format(s))
#             indices.append(s)
#             ''' Sau đó, dịch chuyển chuỗi mẫu 
#             sao cho ký tự tiếp theo trong chuỗi văn bản khớp với xuất hiện cuối cùng của nó trong chuỗi mẫu.
#             Shift the pattern so that the next character in text
#             aligns with the last occurrence of it in pattern.
#             The condition s+m < n is necessary for the case when
#             pattern occurs at the end of text
#             '''
#             s += (lp-badChar[ord(text[s+lp])] if s+lp < lt else 1)
            
#         else:
#             '''Nếu chuỗi mẫu không xuất hiện tại dịch chuyển hiện tại,
# thì dịch chuyển chuỗi mẫu sao cho ký tự “xấu” trong chuỗi văn bản khớp với xuất hiện cuối cùng của nó trong chuỗi mẫu.
#             Shift the pattern so that the bad character in text
#             aligns with the last occurrence of it in pattern. The
#             max function is used to make sure that we get a positive
#             shift. We may get a negative shift if the last occurrence
#             of bad character in pattern is on the right side of the
#             current character.
#             '''
#             s += max(1, j-badChar[ord(text[s+j])])

#     return indices

# def main():
#     text = "ABCABAAABCD"
#     pattern = "ABC"
#     occurrences = search(text, pattern)
#     print("Pattern found at index", occurrences)

# if __name__ == '__main__':
#     main()

# Boyer Moore Algorithm with 
# Good Suffix heuristic to find pattern in 
# given text string
# preprocessing for strong good suffix rule
'''
Hàm này tiền xử lý chuỗi mẫu để tạo ra mảng shift và bpos cho quy tắc hậu tố tốt. 
shift lưu số lượng dịch chuyển cần thiết cho mỗi vị trí trong chuỗi mẫu,
và bpos lưu vị trí của biên phải nhất có thể tìm thấy cho mỗi vị trí trong chuỗi mẫu.
'''
def preprocess_strong_suffix(shift, bpos, pat, lp):
# Khởi tạo i và j để duyệt qua chuỗi mẫu từ phải sang trái. bpos[i] lưu vị trí của biên phải nhất có thể tìm thấy.
	i = lp
	j = lp + 1
	bpos[i] = j

	while i > 0:
		
		'''Vòng lặp này tìm kiếm biên trong chuỗi mẫu. 
        Nếu ký tự tại i-1 không khớp với ký tự tại j-1, 
        thì cập nhật shift[j] nếu chưa được cập nhật, và di chuyển j đến biên tiếp theo
        if character at position i-1 is 
		not equivalent to character at j-1, 
		then continue searching to right 
		of the pattern for border '''
		while j <= lp and pat[i - 1] != pat[j - 1]:
			
			''' the character preceding the occurrence 
			of t in pattern P is different than the 
			mismatching character in P, we stop skipping
			the occurrences and shift the pattern 
			from i to j '''
			if shift[j] == 0:
				shift[j] = j - i

			# Update the position of next border
			j = bpos[j]
			
		''' Nếu hai ký tự khớp, thì giảm i và j và cập nhật bpos[i].
        p[i-1] matched with p[j-1], border is found. 
		store the beginning position of border '''
		i -= 1
		j -= 1
		bpos[i] = j

# Preprocessing for case 2
# Hàm này xử lý trường hợp 2 của quy tắc hậu tố tốt, khi không có hậu tố nào khớp với hậu tố của chuỗi mẫu.
def preprocess_case2(shift, bpos, pat, lp):
	j = bpos[0]
	for i in range(lp + 1):
		
		'''Vòng lặp này cập nhật mảng shift cho trường hợp 2. 
        Nếu shift[i] chưa được cập nhật (vẫn bằng 0), thì cập nhật nó bằng j.
        set the border position of the first character 
		of the pattern to all indices in array shift
		having shift[i] = 0 '''
		if shift[i] == 0:
			shift[i] = j
			
		''' Nếu i bằng j, thì cập nhật j bằng bpos[j].
        suffix becomes shorter than bpos[0], 
		use the position of next widest border
		as value of j '''
		if i == j:
			j = bpos[j]

'''Search for a pattern in given text using 
Boyer Moore algorithm with Good suffix rule '''
def search(text, pat):

	# s is shift of the pattern with respect to text
    
	s = 0 # s là số lượng dịch chuyển của chuỗi mẫu so với chuỗi văn bản
	lp = len(pat)
	lt = len(text)

	bpos = [0] * (lp + 1)

	# initialize all occurrence of shift to 0
	shift = [0] * (lp + 1)

	# do preprocessing
	preprocess_strong_suffix(shift, bpos, pat, lp)
	preprocess_case2(shift, bpos, pat, lp)

	while s <= lt - lp:
		j = lp - 1
		
		''' Keep reducing index j of pattern while characters of 
			pattern and text are matching at this shift s'''
		while j >= 0 and pat[j] == text[s + j]:
			j -= 1
			
		''' If the pattern is present at the current shift, 
			then index j will become -1 after the above loop '''
		if j < 0:
			print("pattern occurs at shift = %d" % s)
			s += shift[0]
		else:
			
			'''pat[i] != pat[s+j] so shift the pattern 
			shift[j+1] times '''
			s += shift[j + 1]


if __name__ == "__main__":
	text = "ABAAAABAACD"
	pat = "ABA"
	search(text, pat)

