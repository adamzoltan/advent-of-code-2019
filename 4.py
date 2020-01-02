low = 248345
high = 746315

def check_never_decrease(num):
    num_str = str(num)
    for i in range(5):
        if int(num_str[i]) > int(num_str[i+1]):
            return False
    return True

def check_equal_adjacents(num):
    num_str = str(num)
    for i in range(5):
        if int(num_str[i]) == int(num_str[i+1]):
            return True
    return False

increasing_nums = [n for n in range(low, high + 1) if check_never_decrease(n)]
equal_adjacents_nums = [n for n in increasing_nums if check_equal_adjacents(n)]

print(len(equal_adjacents_nums))