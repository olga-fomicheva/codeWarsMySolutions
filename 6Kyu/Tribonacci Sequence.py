def tribonacci(signature, n):
    final_list = []
    repeat = 0
    index = 0
    index2 = 0

    for i in range(len(signature)):
        if n > 0:
            while repeat <= n-1:
                if index <= 2:
                    final_list.append(signature[index])
                    index += 1
                    repeat += 1
                else:
                    sum = final_list[index2]+final_list[index2+1]+final_list[index2+2]
                    final_list.append(sum)
                    repeat += 1
                    index2 += 1
        else:
            return []
    return(final_list)
