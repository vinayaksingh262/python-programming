# count the number of digit in an integer
num = 5873
count = 0
while num > 0:
    num = num % 10
    count += num

print(num)
