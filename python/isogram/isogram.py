def is_isogram(string):
    string = string.translate(None, '- ')
    return len(string) == len(set(string.lower()))
