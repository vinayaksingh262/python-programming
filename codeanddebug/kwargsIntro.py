def fun(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}:{v}")


fun(name="vinayak", age=21)
