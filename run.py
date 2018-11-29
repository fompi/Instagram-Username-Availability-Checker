from requests import get
from time import sleep


def available(q):
    url = f'https://insta-node.herokuapp.com/_validate_username?username={q}'
    r = get(url).json()
    return r['valid']


with open('words.txt') as a, open('available.txt', 'a+') as b:
    for word in a.readlines():
        w = word.strip()
        if available(w):
            b.write(word)
            print(w)
