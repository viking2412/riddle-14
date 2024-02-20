from pathlib import Path


def fileread():
    return Path("14.txt").read_text().splitlines()


def transpose(matrix):
    return list(zip(*matrix))


def rotate(matrix):
    new_matrix = []
    for line in list(zip(*matrix)):
        new_matrix.append(line[::-1])
    return new_matrix


def counter(matrix):
    result = 0
    for i, line in enumerate(matrix):
        for ch in line:
            if ch == "O":
                result += i+1
    return result


def sort_2(matrix):
    new_matrix = []
    for line in matrix:
        count = 0
        new_line = []
        for ch in line:
            match ch:
                case "O":
                    if count == 0:
                        new_line.append("O")
                    else:
                        new_line.insert(-count, "O")
                case ".":
                    count += 1
                    new_line.append(".")
                case "#":
                    new_line.append("#")
                    count = 0
        new_matrix.append(new_line)
    return new_matrix


def solve():
    check = {}
    lines = fileread()
    lines = sort_2(transpose(lines))
    lines = sort_2(transpose(lines))
    lines = sort_2(rotate(lines))
    lines = sort_2(rotate(lines))
    check[tuple([tuple(line) for line in lines])] = 0
    for i in range(1, 1000000000):
        lines = sort_2(rotate(lines))
        lines = sort_2(rotate(lines))
        lines = sort_2(rotate(lines))
        lines = sort_2(rotate(lines))
        t_line = tuple([tuple(line) for line in lines])
        if t_line in check:
            result = (1000000000 - check[t_line]) % (i-check[t_line]) + check[t_line] - 1
            break
        check[t_line] = i
    for key, value in check.items():
        if value == result:
            print(counter(key))


if __name__ == '__main__':
    solve()
