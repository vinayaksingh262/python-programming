# head recursion
count = 0


def fun():
    global count
    if count == 4:
        return
    count += 1
    print("vinayak")
    fun()


fun()
# tail recursion
count = 0


def fun():
    global count
    if count == 4:
        return
    count += 1
    fun()
    print("vinayak")


fun()
