def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def has_only_prime_digits(num):
    prime_digits = {"2", "3", "5", "7"}
    return all(digit in prime_digits for digit in str(num))


def count_megaprimes(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num) and has_only_prime_digits(num):
            count += 1
    return count


if __name__ == "__main__":

    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    result = count_megaprimes(start, end)
    print(f"The number of MegaPrime numbers between {start} and {end} is: {result}")
