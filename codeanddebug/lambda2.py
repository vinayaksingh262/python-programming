# take a number from user and make a list 0 to n by using Lambda function
make_lst = lambda n: [i for i in range(0, n + 1)]
len = int(input("Enter a length of a list = "))
list1 = make_lst(len)
print(list1)
