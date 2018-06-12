# python 2.7
import re

def decode(string):
    pattern = re.compile('([\d]*)([\w ])')
    groups = re.findall(pattern, string)
    return ''.join([ character * int(times if times else 1)for (times, character) in groups])


def encode(string):
    response = []
    for s in string:
        try:
            data = response[-1]
        except IndexError:
            data = {'size': 0, 'character': s}
            response.append(data)

        if data['character'] == s:
            data = {'size': data['size'] + 1, 'character': s}
            response[-1] = data
        else:
            data = {'size': 1, 'character': s}
            response.append(data)


    return ''.join(
        [
            str(data['size']) + data['character'] if data['size'] > 1 else data['character']
            for data in response
        ]
    )
