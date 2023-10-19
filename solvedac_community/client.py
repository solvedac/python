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

from solvedac_community.HTTPClients import *
from solvedac_community.Schemas import *
from solvedac_community.utils import check_stats_code

__all__ = ["Client"]


class Client:
    __loop: asyncio.AbstractEventLoop
    __http_client: AbstractHTTPClient
    __has_token: bool

    def __init__(self, solvedac_token: Optional[str] = None, http_library: HTTPClientLibrary = None) -> None:
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except AttributeError:
            pass
        self.__loop = asyncio.get_event_loop()
        self.__http_client = get_http_client(self.__loop, solvedac_token=solvedac_token, lib=http_library)
        self.__has_token = bool(solvedac_token)

    async def get_user(self, handle: str) -> Models.User:
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/user/show", params={"handle": handle})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.User(json_data)

    async def get_user_organizations(self, handle: str) -> List[Models.Organization]:
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/user/organizations", params={"handle": handle})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return [Models.Organization(dat) for dat in json_data]

    async def get_user_problem_stats(self, handle: str) -> List[Models.ProblemStats]:
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/user/problem_stats", params={"handle": handle})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return [Models.ProblemStats(dat) for dat in json_data]

    async def get_background(self, background_id: str) -> Models.Background:
        response: ResponseData = await self.__http_client.request(
            Route(
                RequestMethod.GET,
                f"/background/show",
                params={"backgroundId": background_id},
            )
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.Background(json_data)

    async def get_badge(self, badge_id: str) -> Models.Badge:
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/badge/show", params={"badgeId": badge_id})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.Badge(json_data)

    async def get_coins_exchange_rate(self) -> int:
        response: ResponseData = await self.__http_client.request(Route(RequestMethod.GET, f"/coins/exchange_rate"))

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return json_data["rate"]

    async def get_coinshop_products(self) -> List[Models.CoinshopProduct]:
        response: ResponseData = await self.__http_client.request(Route(RequestMethod.GET, f"/coins/shop/list"))

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return [Models.CoinshopProduct(d) for d in json_data]

    async def get_site_stats(self) -> Models.SolvedAcStatistics:
        response: ResponseData = await self.__http_client.request(Route(RequestMethod.GET, f"/site/stats"))

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.SolvedAcStatistics(json_data)

    async def get_problem_by_id(self, problem_id: int) -> Models.TaggedProblem:
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/problem/show", params={"problemId": problem_id})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.TaggedProblem(json_data)

    async def get_problem_by_id_array(self, problem_ids: Iterable[Union[int, str]]) -> List[Models.TaggedProblem]:
        query = ",".join(map(str, problem_ids))
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/problem/lookup", params={"problemIds": query})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return [Models.TaggedProblem(d) for d in json_data]

    async def get_problem_level(self) -> List[Models.ProblemLevelData]:
        response: ResponseData = await self.__http_client.request(Route(RequestMethod.GET, f"/problem/level"))

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return [Models.ProblemLevelData(d) for d in json_data]

    async def search_problem(
        self,
        query: str,
        direction: Union[Enums.SortDirection, str],
        page: int,
        sort: Union[Enums.SortType, str],
    ) -> Models.ProblemSearchData:
        response: ResponseData = await self.__http_client.request(
            Route(
                RequestMethod.GET,
                f"/search/problem",
                params={"query": query, "direction": str(direction), "page": page, "sort": str(sort)},
            )
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.ProblemSearchData(json_data)

    async def get_search_auto_completion(self, query: str) -> Models.AutoCompletionData:
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/search/suggestion", params={"query": query})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.AutoCompletionData(json_data)

    async def verify_account_credentials(self) -> Models.AccountInfo:
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, "/account/verify_credentials")
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.AccountInfo(json_data)

    async def update_account_settings(self, key: str, value: str) -> None:
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.PATCH, "/account/update_settings"), body={"key": key, "value": value}
        )

        check_stats_code(response.status)
