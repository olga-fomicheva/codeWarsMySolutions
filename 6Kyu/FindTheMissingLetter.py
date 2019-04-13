def find_missing_letter(chars):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper = chars[0].isupper()
    chars = [x.lower() if upper == True else x for x in chars]
    letter_position = abc.index((chars[0]))
    abc_cut = abc[letter_position:1+len(chars)+letter_position]
    for char in abc_cut:
        if char not in chars:
            if upper == True:
                return char.upper()
            else:
                return char