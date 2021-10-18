def just(inp, max_w):
    words = inp.split()
    lines = []
    line = []
    output = []

    for w in words:

        if len(" ".join(line)) + (len(w) + 1) > max_w:
            lines.append(line)
            line = [w, ]

        else:
            line.append(w)

    lines.append(line)

    out = []

    for line in lines[:-1]:
        spaces = max_w - sum([len(x) for x in line])
        min_spaces = len(line) - 1
        min_spaces = 1 if min_spaces == 0 else min_spaces

        all_len = spaces // min_spaces
        foo = spaces % min_spaces

        spa = [" " * all_len for x in range(len(line) - 1)]
        for i in range(foo):
            spa[i] += " "

        new = []
        for w in line:
            new.append(w)
            new.append(spa.pop(0)) if len(spa) > 0 else None

        out.append(new)

    out.append(" ".join(lines[-1]))

    for line in out:
        output.append("".join(line))
    return output


def main():
    words = "Hey there mate, it’s nice to finally meet you!"
    maximum_width = 16
    print(just(words, maximum_width))


if __name__ == "__main__":
    main()
