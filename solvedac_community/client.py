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
        """
        사용자의 정보를 가져옵니다.

        :param handle: :class:`str` 사용자 ID
        :return: :class:`Models.User`
        """

        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/user/show", params={"handle": handle})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.User(json_data)

    async def get_user_organizations(self, handle: str) -> List[Models.Organization]:
        """
        사용자가 속한 조직 목록를 가져옵니다.

        :param handle: :class:`str` 사용자 ID
        :return: List[:class:`Models.Organizaion`]
        """

        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/user/organizations", params={"handle": handle})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return [Models.Organization(dat) for dat in json_data]

    async def get_user_problem_stats(self, handle: str) -> List[Models.ProblemStats]:
        """
        사용자가 푼 문제 개수를 문제 수준별로 가져옵니다.

        :param handle: :class:`str` 사용자 ID
        :return: List[:class:`Models.ProblemStats`]
        """

        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/user/problem_stats", params={"handle": handle})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return [Models.ProblemStats(dat) for dat in json_data]

    async def get_background(self, background_id: str) -> Models.Background:
        """
        배경의 정보를 가져옵니다.

        :param background_id: :class:`str` 배경 ID
        :return: :class:`Models.Background`
        """

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
        """
        뱃지의 정보를 가져옵니다.

        :param badge_id: :class:`str` 뱃지 ID
        :return: :class:`Models.Badge`
        """

        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/badge/show", params={"badgeId": badge_id})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.Badge(json_data)

    async def get_coins_exchange_rate(self) -> int:
        """
        현재 코인 -> 별조각 환율을 가져옵니다.

        :return: :class:`int`
        """

        response: ResponseData = await self.__http_client.request(Route(RequestMethod.GET, f"/coins/exchange_rate"))

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return json_data["rate"]

    async def get_coinshop_products(self) -> List[Models.CoinshopProduct]:
        """
        코인샵에서 팔고 있는 상품 목록을 가져옵니다.

        :return: List[:class:`Models.CoinshopProduct`]
        """

        response: ResponseData = await self.__http_client.request(Route(RequestMethod.GET, f"/coins/shop/list"))

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return [Models.CoinshopProduct(d) for d in json_data]

    async def get_site_stats(self) -> Models.SolvedAcStatistics:
        """
        solved.ac 통계를 가져옵니다.

        :return: :class:`Models.SolvedAcStatistics`
        """

        response: ResponseData = await self.__http_client.request(Route(RequestMethod.GET, f"/site/stats"))

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.SolvedAcStatistics(json_data)

    async def get_problem_by_id(self, problem_id: int) -> Models.TaggedProblem:
        """
        해당하는 ID의 문제를 가져옵니다.

        :param problem_id: :class:`int` 문제 ID
        :return: :class:`Models.TaggedProblem`
        """

        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/problem/show", params={"problemId": problem_id})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.TaggedProblem(json_data)

    async def get_problem_by_id_array(self, problem_ids: Iterable[Union[int, str]]) -> List[Models.TaggedProblem]:
        """
        해당하는 ID의 문제 목록을 가져옵니다.

        :param problem_ids: Iterable[Union[:class:`int`, :class:`str`]]  문제 ID 목록
        :return: List[:class:`Models.TaggedProblem`]
        """

        query = ",".join(map(str, problem_ids))
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/problem/lookup", params={"problemIds": query})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return [Models.TaggedProblem(d) for d in json_data]

    async def get_problem_level(self) -> List[Models.ProblemLevelData]:
        """
        문제 개수를 문제 수준별로 가져옵니다.

        :return: List[:class:`Models.ProblemLevelData`]
        """

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
        """
        주어진 쿼리에 따라 문제를 검색합니다.

        :param query: :class:`str` 쿼리 문자열
        :param direction: Union[:class:`Enums.SortDirection`, :class:`str`] 정렬 방향
        :param page: :class:`int` 페이지
        :param sort: Union[:class:`Enums.SortType`, :class:`str`] 정렬 기준
        :return: :class:`Models.ProblemSearchData`
        """

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
        """
        주어진 쿼리에 따라 검색해보고, 자동 완성에 적합하도록 가공한 정보를 돌려줍니다.

        :param query: :class:`str` 쿼리 문자열
        :return: :class:`Models.AutoCompletionData`
        """

        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.GET, f"/search/suggestion", params={"query": query})
        )

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.AutoCompletionData(json_data)

    async def verify_account_credentials(self) -> Models.AccountInfo:
        """
        현재 로그인한 계정 정보를 가져옵니다.

        :return: :class:`Models.AccountInfo`
        """

        response: ResponseData = await self.__http_client.request(Route(RequestMethod.GET, "/account/verify_credentials"))

        check_stats_code(response.status)

        json_data: dict = json.loads(response.response_data)
        return Models.AccountInfo(json_data)

    async def update_account_settings(self, key: str, value: str) -> None:
        """
        계정의 설정을 변경합니다.

        :param key: :class:`str` 업데이트할 설정의 이름입니다.
        :param value: :class:`str` 업데이트할 설정의 새로운 값입니다.
        """
        response: ResponseData = await self.__http_client.request(
            Route(RequestMethod.PATCH, "/account/update_settings"), body={"key": key, "value": value}
        )

        check_stats_code(response.status)
