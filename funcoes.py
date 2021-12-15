def add(y, z):
    x = int(y) + int(z)
    return x


def sub(y, z):
    x = int(y) - int(z)
    return x


def mult(y, z):
    x = int(y) * int(z)
    return x


def div(y, z):
    try:
        x = int(y) / int(z)
    except ZeroDivisionError:
        x = "Impossible"
    return x


def pot(y, z):
    x = int(y) ** int(z)
    return x
