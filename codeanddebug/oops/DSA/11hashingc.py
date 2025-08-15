s = "azyxyyzaaaa"
q = ["a", "d", "y", "x"]
hash_lst = [0] * 26
for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_lst[index] += 1
for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print("the letter", ch, "appears", hash_lst[index], "times.")
