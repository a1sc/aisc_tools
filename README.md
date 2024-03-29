![AISC](http://aisc.io/wp-content/uploads/2018/09/logo.svg)

## AISC Tools

[![CircleCI](https://img.shields.io/circleci/build/github/a1sc/aisc_tools.svg?label=CircleCI)](https://circleci.com/gh/a1sc/aisc_tools)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aisc.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/a1sc/aisc_tools.svg)
[![PyPI](https://img.shields.io/pypi/v/aisc.svg)](https://pypi.org/project/aisc/)

Small helper tools.

## Installation

`pip install aisc`

## URL Tools

```python3
from aisc import url
```

#### Expand shortened url
`url.expand(url)`

#### Replace params in url
```python3
url.replace('http://example.com?foo=bar', {'foo': 'spam'})
>>> 'http://example.com?foo=spam'
```

