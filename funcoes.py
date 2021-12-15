def add(y, z):
    x = y + z
    print(x)
    return


def sub(y, z):
    x = y - z
    return x


def mult(y, z):
    x = y * z
    return x


def div(y, z):
    try:
        x = y / z
    except ZeroDivisionError:
        x = "Impossible"
    return x


def pot(y, z):
    x = y ** z
    return x
