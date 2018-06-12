import re

MAX_NUMBERS_ISBN = 10

def verify(isbn):
    patterns = [
        re.compile('([\d]{1})-([\d]{3})-([\d]{5})-([\dX]{1})$'),
        re.compile('([\d]{9})([\dX]{1})$'),
    ]
    for pattern in patterns:
        match = pattern.match(isbn)
        if match:
            current_value = 0

            digits = sum([list(group) for group in match.groups()], [])
            digits_validators = range(MAX_NUMBERS_ISBN, 0, -1)
            for digit, digit_validator in zip(digits, digits_validators):
                try:
                    digit = int(digit)
                except ValueError:
                    digit = 10
                current_value +=  digit * digit_validator

            return current_value % 11 == 0
    return False
