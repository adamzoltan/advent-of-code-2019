wire_1 = []
wire_2 = []

with open("wire_1.txt", "r") as filestream:
    for line in filestream:
        current_line = line.split(",")
        for words in current_line:
            wire_1.append(words)

with open("wire_2.txt", "r") as filestream:
    for line in filestream:
        current_line = line.split(",")
        for words in current_line:
            wire_2.append(words)
