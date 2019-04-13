def alphabet_position(text):
    print(text)
    order =  [ord(x) for x in text if x.isalpha()]
    new_text = ""
    for each in order:
        location = each - 64 if each >= 64 and each <= 90 else each - 96
        new_text += str(location)+" "
    return new_text.strip()