# count the number of digit in an integer
def countDigit(n: int):

    count = 0
    while n > 0:

        count += 1
        n = n // 10
    print(count)


n = int(input("Enter a integer you want to count digit: "))
countDigit(n)
