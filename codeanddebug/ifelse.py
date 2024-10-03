held=int(input("no of class held :"))
atnd=int(input("no of class attend :"))
per=atnd/held*100
print(f"total percentage of attendance :{per:.2f}%")
if per>=75:
    print("eligible for exam.")
else:
    print("not eligible!")