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


def sort(line):
    count = 0
    new_line = []
    load = 0
    for ch in line:
        match ch:
            case "O":
                if count == 0:
                    new_line.append("O")
                    load += len(line) - (len(new_line)-1)
                else:
                    new_line.insert(-count, "O")
                    load += len(line) - (len(new_line)-1-count)
            case ".":
                count += 1
                new_line.append(".")
            case "#":
                new_line.append("#")
                count = 0
    return load


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
    #for _ in range(1000000000):

    lines = fileread()
    lines = sort_2(transpose(lines))
    lines = sort_2(transpose(lines))
    lines = sort_2(rotate(lines))
    lines = sort_2(rotate(lines))
    for _ in range(1000000000):
        lines = sort_2(rotate(lines))
        lines = sort_2(rotate(lines))
        lines = sort_2(rotate(lines))
        lines = sort_2(rotate(lines))
    sort(lines)
    print("done!")



if __name__ == '__main__':
    solve()

# 13  12  31  43  12
# 24  34  42  21  34
# n   w   s   e