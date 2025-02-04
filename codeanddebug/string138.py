# wap to reverse the order of words
my_str = "python is good "
words = my_str.split()
words = words[::-1]
result = " ".join(words)
print(result)
