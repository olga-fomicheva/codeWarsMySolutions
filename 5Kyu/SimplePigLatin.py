from string import ascii_letters


def pig_it(text):
    spec_chars = ['!', '?', '.', ',', ':', ';', '#', '@']
    new_sentence = ''
    for each in text.split():
        if each not in spec_chars:
            renew = each[1:] + each[0] + 'ay'
            new_sentence += renew + ' '
        else:
            new_sentence += each
    return new_sentence.strip()
