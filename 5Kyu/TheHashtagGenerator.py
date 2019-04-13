def generate_hashtag(s):
    hashtag = '#'
    if len(s) == 0:
        return False
    for words in s.split():
        hashtag += words.capitalize()
    if len(hashtag) >= 140:
        return False
    else:
        return hashtag