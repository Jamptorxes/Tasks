def reverse(x: int):

    try:
        if not -(2 ** 31) < x < 2 ** 31 - 1:
            return 0
        number = str(x)
        if number[0] == "-":
            return int(number[:0:-1]) * -1
        return int(number[::-1])

    except (KeyError, ValueError, TypeError):
        return "X variable must be integer!"


def main():
    x = -865
    print(reverse(x))


if __name__ == "__main__":
    main()
