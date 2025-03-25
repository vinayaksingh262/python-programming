import multiprocessing


def print_cube(num):
    print(f"cube{num**3}")


def print_square(num):
    print(f"squre{num**2}")


p1 = multiprocessing.Process(taret=print_cube, args=(10,))
p2 = multiprocessing.Process(target=print_square, args=(10,))
p1.start()
p2.start
p1.join()
p2.join()
