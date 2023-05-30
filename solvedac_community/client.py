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
import json
from typing import Optional, List, Iterable, Union

from .HTTPClients import *
from .Models import *


class Client:
    loop: asyncio.AbstractEventLoop
    http_client: AbstractHTTPClient

    def __init__(self, solvedac_token: Optional[str] = None, http_library: HTTPClientLibrary = None) -> None:
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except AttributeError:
            pass
        self.loop = asyncio.get_event_loop()
        self.http_client = get_http_client(self.loop, solvedac_token=solvedac_token, lib=http_library)

    async def get_user(self, handle: str) -> User:
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/user/show", params={"handle": handle})
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return User(json_data)

    async def get_user_organizations(self, handle: str) -> List[Organization]:
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/user/organizations", params={"handle": handle})
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return [Organization(dat) for dat in json_data]

    async def get_user_problem_stats(self, handle: str) -> List[ProblemStats]:
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/user/problem_stats", params={"handle": handle})
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return [ProblemStats(dat) for dat in json_data]

    async def get_background(self, background_id: str) -> Background:
        response: ResponseData = await self.http_client.request(
            Route(
                RequestMethod.GET,
                f"/background/show",
                params={"backgroundId": background_id},
            )
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return Background(json_data)

    async def get_badge(self, badge_id: str) -> Badge:
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/badge/show", params={"badgeId": badge_id})
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return Badge(json_data)

    async def get_coins_exchange_rate(self) -> int:
        response: ResponseData = await self.http_client.request(Route(RequestMethod.GET, f"/coins/exchange_rate"))
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return json_data["rate"]

    async def get_coinshop_products(self) -> List[CoinshopProduct]:
        response: ResponseData = await self.http_client.request(Route(RequestMethod.GET, f"/coins/shop/list"))
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return [CoinshopProduct(d) for d in json_data]

    async def get_site_stats(self) -> SolvedAcStatistics:
        response: ResponseData = await self.http_client.request(Route(RequestMethod.GET, f"/site/stats"))
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return SolvedAcStatistics(json_data)

    async def get_problem_by_id(self, problem_id: int) -> TaggedProblem:
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/problem/show", params={"problemId": problem_id})
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return TaggedProblem(json_data)

    async def get_problem_by_id_array(self, problem_ids: Iterable[Union[int, str]]) -> List[TaggedProblem]:
        query = ",".join(map(str, problem_ids))
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/problem/lookup", params={"problemIds": query})
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return [TaggedProblem(d) for d in json_data]

    async def get_problem_level(self) -> List[ProblemLevelData]:
        response: ResponseData = await self.http_client.request(Route(RequestMethod.GET, f"/problem/level"))
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return [ProblemLevelData(d) for d in json_data]

    async def search_problem(
        self,
        query: str,
        direction: Union[SortDirection, str],
        page: int,
        sort: Union[SortType, str],
    ) -> ProblemSearchData:
        response: ResponseData = await self.http_client.request(
            Route(
                RequestMethod.GET,
                f"/search/problem",
                params={"query": query, "direction": str(direction), "page": page, "sort": str(sort)},
            )
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return ProblemSearchData(json_data)

    async def get_search_auto_completion(self, query: str) -> AutoCompletionData:
        response: ResponseData = await self.http_client.request(
            Route(RequestMethod.GET, f"/search/suggestion", params={"query": query})
        )
        assert response.status == 200, "HTTP Response Status Code is not 200\nStatus Code : %d" % response.status
        json_data: dict = json.loads(response.response_data)
        return AutoCompletionData(json_data)
