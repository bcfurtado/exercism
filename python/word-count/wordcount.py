
def word_count(string):
    words = string.lower().split()
    return {word: words.count(word) for word in words}