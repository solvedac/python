# -*- coding: utf-8 -*-

"""
SolvedAC API Wrapper
~~~~~~~~~~~~~~~~~~~

https://solvedac.github.io/unofficial-documentation/#/

An API Wrapper for SolvedAC API

Copyright (c) 2023 DevRuby
"""

from .client import Client

count = 0

try:
    import aiohttp
    count += 1
except ImportError:
    pass

try:
    import httpx
    count += 1
except ImportError:
    pass

if count == 0:
    raise ImportError("\nAt least one of aiohttp or httpx libraries is required\nTry `pip install aiohttp` or `pip install httpx`")