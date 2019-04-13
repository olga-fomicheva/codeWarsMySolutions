def spin_words(sentence):
    reversed_sentence = [x[::-1] if len(x) >= 5 else x for x in sentence.split() ]
    return " ".join(reversed_sentence)