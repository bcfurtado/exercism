from string import ascii_lowercase, ascii_uppercase, maketrans, translate


def cipher(text, from_table, to_table):
    translation_table = maketrans(from_table, to_table)
    return translate(text, translation_table)


def rotate(text, key):
    to_lowercase = ascii_lowercase[key:] + ascii_lowercase[:key]
    to_uppercase = ascii_uppercase[key:] + ascii_uppercase[:key]
    text = cipher(text, ascii_lowercase, to_lowercase)
    return cipher(text, ascii_uppercase, to_uppercase)
