# -*- coding: utf-8 -*-

"""
Copyright (c) 2023 DevRuby
MIT License
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

from .abstract_http_client import AbstractHTTPClient
from .httpclient import RequestMethod
from .httpclient import ResponseData
from .httpclient import Route
from .httpclient import get_http_client

__all__ = ["AbstractHTTPClient", "RequestMethod", "ResponseData", "Route", "get_http_client"]

try:
    from .aiohttp_client import AiohttpHTTPClient

    __all__.append("AiohttpHTTPClient")
except ImportError:
    pass

try:
    from .httpx_client import HttpxHTTPClient

    __all__.append("HttpxHTTPClient")
except ImportError:
    pass
