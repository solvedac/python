# -*- coding: utf-8 -*-

"""
SolvedAC API Wrapper
~~~~~~~~~~~~~~~~~~~

https://solvedac.github.io/unofficial-documentation/#/

An API Wrapper for SolvedAC API

Copyright (c) 2023 DevRuby
"""

from . import HTTPClients
from .client import Client

__all__ = ["Client", "HTTPClients"]
