import requests


def send_request(url: str) -> str:
    """Sending request and put it into the string"""
    response = requests.get(url)
    a = response.text.rstrip()
    return a


def counter(string: str) -> dict:
    """Pop a dictionary with each character and its occurrences in a string. Key - character, value - occurrence"""
    res = {char: string.count(char) for char in string.rstrip()}
    return res


def result(res: dict) -> str:
    """Write date from dictionary into the file"""
    with open('Task_3/readme.md', 'w') as f:
        for key, value in res.items():
            f.write(f"'{key}': {str(value)}\n")
    return 'Success'

text = "https://www.python.org/"
print(result(counter(send_request(text))))
