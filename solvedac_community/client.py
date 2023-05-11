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

import asyncio
from typing import Optional

from .httpclient import HTTPClient


class Client:
    loop: asyncio.AbstractEventLoop
    http_client: HTTPClient

    def __init__(self, solvedac_token: Optional[str] = None) -> None:
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except AttributeError:
            pass
        self.loop = asyncio.get_event_loop()
        self.http_client = HTTPClient(self.loop, solvedac_token)
