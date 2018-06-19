from string import ascii_lowercase, ascii_uppercase, maketrans, translate


def rotate(text, key):
    to_lowercase = ascii_lowercase[key:] + ascii_lowercase[:key]
    to_uppercase = ascii_uppercase[key:] + ascii_uppercase[:key]
    translation_table = maketrans(ascii_lowercase + ascii_uppercase, to_lowercase + to_uppercase)
    return translate(text, translation_table)
