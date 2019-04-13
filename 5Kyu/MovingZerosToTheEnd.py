def move_zeros(array):
    zeros = [x for x in array if x == 0 and type(x) == int or type(x) == float]
    non_zeros = [x for x in array if x != 0 or x is False]
    return non_zeros + zeros