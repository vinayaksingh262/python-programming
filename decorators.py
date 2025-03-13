def my_deco(func):
    def wrapper():
        print("something befor the func runs...")
        func()
        print("something after the func runs...")

    return wrapper


@my_deco
def say_hello():
    print("hello ji")


say_hello()
