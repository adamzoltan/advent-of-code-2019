input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]

def gravity_restore(inp):
    inp[1] = 12
    inp[2] = 2
    return inp

def intcode(inp):
    position = 0
    while inp[position] != 99:
        value_1 = inp[inp[position+1]]
        value_2 = inp[inp[position+2]]
        if inp[position] == 1:
            summary = value_1 + value_2
            inp[inp[position+3]] = summary
        if inp[position] == 2:
            product = value_1 * value_2
            inp[inp[position+3]] = product
        position += 4
    return inp


def intcode_pt2():
    for n in range(100):
        for v in range(100):
            inp = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]
            inp[1] = n
            inp[2] = v
            ret = intcode(inp)
            if ret[0] == 19690720:
                print(f"noun: {n}, verb: {v}")


if __name__ == "__main__":
    inp_numbers = gravity_restore(input)
    result = intcode(inp_numbers)
    print(result)

    intcode_pt2()