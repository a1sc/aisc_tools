import requests


def url_expand(url: str) -> str:
    r = requests.get(url)
    return r.url
