file_name = input("enter a file name (without extension) =")
file_name = file_name + ".txt"
with open(file_name, "w") as f:
    while True:
        sentence = input("enter a sentence =")
        if sentence == "q" or sentence == "Q":
            break
        f.write(sentence)
        f.write("\n")
