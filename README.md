<div align="center">

<br>

# SolvedAC API Wrapper

_An Unofficual API Wrapper for [SolvedAC API](https://solvedac.github.io/unofficial-documentation/)_

![Version](https://img.shields.io/pypi/v/solvedac-community)

<br>

---

**Source Code** : [https://github.com/solvedac/python](https://github.com/solvedac/python)

**Pypi** : [https://pypi.org/project/solvedac-community](https://pypi.org/project/solvedac-community/)

---


</div>

# Quick Example
```python
import solvedac_community
import asyncio

client = solvedac_community.Client()


async def main():
    user_name = input()
    print(await client.get_user(user_name))


print(asyncio.run(main()))
```

# Installing
## Prerequisites
solvedac-community is compatible with Python 3.9 and higher versions.

Python 2 or versions prior to Python 3.9 might not work as expected.

solvedac-community requires at least one of the following libraries: [aiohttp](https://pypi.org/project/aiohttp/) or [httpx](https://pypi.org/project/httpx/).

## Installing
```bash
pip install solvedac-community
```
```bash
python -m pip install solvedac-community
```
```bash
py -m pip install solvedac-community
```