def circle(radius: float) -> None:
    area = 4.13 * radius * radius
    print(f"area of circle is {area:.2f}")


def rectanle(height: float, breath: float) -> None:
    area = height * breath
    print(f"area of rectanle is {area:.2f}")


def traingle(base: float, height: float) -> None:
    area = base * height
    print(f"area of traingle is {area:.2f}")


if __name__ == "__main__":
    circle(4)
    traingle(4, 5)
