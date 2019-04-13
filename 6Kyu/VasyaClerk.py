def tickets(people):
    count_25 = 0
    count_50 = 0

    for each in people:
        if each == 25:
            count_25 += 1
        elif each == 50:
            if count_25 > 0:
                count_25 -= 1
                count_50 += 1
            else:
                return "NO"
        elif each == 100:
            if count_25 >= 1 and count_50 >= 1:
                count_25 -= 1
                count_50 -= 1
            elif count_25 >= 3:
                count_25 -= 3
            else:
                return "NO"
    return "YES"