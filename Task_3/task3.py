import requests


def send_request(url: str) -> str:
    response = requests.get(url)
    a = response.text.rstrip()
    return a


def counter(string: str) -> dict:
    res = {char: string.count(char) for char in string.rstrip()}
    return res


def result(res):
    with open('readme.md', 'w') as f:
        for key, value in res.items():
            f.write(f"'{key}': {str(value)}\n")
    return 'Success'

text = "https://www.python.org/"
print(result(counter(send_request(text))))
