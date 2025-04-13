from collections import Counter
import matplotlib.pyplot as plt

text = "aaabbbsbshxhxhhbssjbsjs"
counter = Counter(text)

letters = list(counter.keys())
counts = list(counter.values())
plt.bar(letters, counts, color="skyblue")
plt.title("Character Frequency")
plt.xlabel("Characters")
plt.ylabel("Frequency")
plt.show()
