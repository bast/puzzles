from collections import defaultdict


def read_input(file_name):
    data = defaultdict(str)
    with open(file_name, "r") as f:
        for row, line in enumerate(f.read().splitlines()):
            for col, c in enumerate(line):
                data[(row, col)] = c
    return data


def accessible_points(point, data):
    points = []
    (x, y) = point
    for (dx, dy) in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        if not data[(x + dx, y + dy)] == "*":
            for i in range(1, 10):
                ap = (x + i * dx, y + i * dy)
                if data[ap] == str(i):
                    points.append(ap)
    return points


def find_path(point, path, data, visited):
    for ap in accessible_points(point, data):
        _path = list(path)
        if ap == (11, 11):
            _path.append(ap)
            print_solution(list(reversed(_path)), data)
        else:
            if not ap in visited:
                visited.add(ap)
                _path.append(ap)
                find_path(ap, _path, data, visited)


def print_solution(path, data):
    print()
    for ((x1, y1), (x2, y2)) in zip(path, path[1:]):
        text = ""
        if x1 < x2:
            text += "S"
        elif x1 > x2:
            text += "N"
        if y1 < y2:
            text += "E"
        elif y1 > y2:
            text += "W"
        distance = max(abs(x2 - x1), abs(y2 - y1))
        print(text, distance)


if __name__ == "__main__":
    data = read_input("data.txt")

    bounds = [k for (k, v) in data.items() if v == "*"]

    for point in bounds:
        visited = set()
        find_path(point, [point], data, visited)
