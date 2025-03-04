"""Like other languages  do, python does not support method overloading by default.
 But there are different ways to achieve method overloading in Python. """

"""By Using Multiple Dispatch Decorator """
from multipledispatch import dispatch


@dispatch(int, int)
def product(first, second):
    return print(f"{first * second}")


@dispatch(int, int, int)
def product(first, second, third):
    return print(f"{first * second * third}")


@dispatch(int, int, int, int)
def product(first, second, third, fourth):
    return print(f"{first * second * third * fourth}")


product(10, 20)
product(10, 20, 30)
product(10, 20, 30, 40)
