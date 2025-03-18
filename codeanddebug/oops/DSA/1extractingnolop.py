# extract and print each digit of given integer number starting from the last digit
def extractDigit(num: int) -> None:

    n = num
    while n > 0:
        last_digit = n % 10
        print(last_digit, end="")
        n = n // 10


extractDigit(5473)
