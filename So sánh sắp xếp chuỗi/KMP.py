def compute_lps(pattern):
    lps = [0] * len(pattern) # Longest Proper Prefix which is also suffix
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    lp = len(pattern)
    lt = len(text)
    lps_pattern = compute_lps(pattern)
    i = j = 0
    
    while i < lt:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == lp:
                print("Pattern found at index", i - j)
                j = lps_pattern[j - 1]
        else:
            if j != 0:
                j = lps_pattern[j - 1]
            else:
                i += 1


text = input()
pattern = input()
#print (compute_lps("ABCABDABC"))
kmp_search(text, pattern)