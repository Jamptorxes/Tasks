def dial(digits: str):
    try:
        if not digits:
            return []

        keys = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
            0: "",
        }

        out = [""]

        for digit in digits:
            temp = []
            for key in keys[int(digit)]:
                temp += [o + key for o in out]
            out = temp
        return out

    except (KeyError, ValueError, TypeError):
        return "Digits must be list/string of integers from range 0-9"


def main():
    digits = "46"
    print(dial(digits))


if __name__ == "__main__":
    main()
