from aisc import url


def test_expand():
    short_url = "http://bit.ly"
    expanded_url = "https://bitly.com/"
    assert url.expand(short_url) == expanded_url
