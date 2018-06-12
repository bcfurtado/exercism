from string import ascii_lowercase as letters

def is_pangram(sentence):
    return set(letters).issubset(str(sentence.lower()))
