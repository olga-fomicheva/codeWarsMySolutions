from collections import Counter

def delete_nth(order, max_e):
    cnt = Counter()
    new_arr = []
    for each in order:
        cnt[each] += 1
        if cnt[each] <= max_e:
            new_arr.append(each)
        else:
            pass

    return new_arr