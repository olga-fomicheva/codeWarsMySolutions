def kebabize(string):
    new_string = ''
    string = ''.join([i for i in string if not i.isdigit()])
    for index, each in enumerate(string):
        if each.isupper() and index != 0:
            new_string += "-"+each.lower()
        else:
            new_string += each.lower()
    return new_string