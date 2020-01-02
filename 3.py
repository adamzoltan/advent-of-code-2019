wire_1_path = []
wire_2_path = []

with open("wire_1.txt", "r") as filestream:
    for line in filestream:
        current_line = line.rstrip('\n').split(",")
        for words in current_line:
            wire_1_path.append(words)

with open("wire_2.txt", "r") as filestream:
    for line in filestream:
        current_line = line.rstrip('\n').split(",")
        for words in current_line:
            wire_2_path.append(words)

DX = {"L": -1, "R": 1, "U": 0, "D": 0}
DY = {"L": 0, "R": 0, "U": 1, "D": -1}

def get_coordinates(wire_path):
    x = 0
    y = 0
    wire_coordinates = set()
    for path in wire_path:
        direction = path[0]
        steps = int(path[1:])
        for _ in range(steps):
            x += DX[direction]
            y += DY[direction]
            wire_coordinates.add((x, y))
    return wire_coordinates

points_1 = get_coordinates(wire_1_path)
points_2 = get_coordinates(wire_2_path)
common = points_1 & points_2
ans = min([abs(x) + abs(y) for (x, y) in common])
print(ans)