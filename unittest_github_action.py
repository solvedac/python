import solvedac_community as SolvedAC
import asyncio
import unittest

loop = asyncio.get_event_loop()

client = SolvedAC.Client()

user_list = ["devruby"]

background_list = [
    "users_100k"
]

badge_list = ["ghudegy2023"]

query_list = ["graph"]

search_query_list = zip(
    ("tree",),
    ("asc",),
    (1,),
    ("id",),
)

problem_id_array_list = [
    [1000, 1001, 1002, 1003, 1004],
]

problem_id_list = [1000]

DEBUG = True


class Test(unittest.TestCase):
    def test_get_user(self):
        for user in user_list:
            if DEBUG:
                print(loop.run_until_complete(client.get_user(user)))
            else:
                (loop.run_until_complete(client.get_user(user)))

    def test_get_user_organizations(self):
        for user in user_list:
            if DEBUG:
                print(loop.run_until_complete(client.get_user_organizations(user)))
            else:
                (loop.run_until_complete(client.get_user_organizations(user)))

    def test_get_user_problem_stats(self):
        for user in user_list:
            if DEBUG:
                print(loop.run_until_complete(client.get_user_problem_stats(user)))
            else:
                (loop.run_until_complete(client.get_user_problem_stats(user)))

    def test_get_background(self):
        for background in background_list:
            if DEBUG:
                print(loop.run_until_complete(client.get_background(background)))
            else:
                (loop.run_until_complete(client.get_background(background)))

    def test_get_badge(self):
        for badge in badge_list:
            if DEBUG:
                print(loop.run_until_complete(client.get_badge(badge)))
            else:
                (loop.run_until_complete(client.get_badge(badge)))

    def test_get_coins_exchange_rate(self):
        if DEBUG:
            print(loop.run_until_complete(client.get_coins_exchange_rate()))
        else:
            (loop.run_until_complete(client.get_coins_exchange_rate()))

    def test_get_coin_shop_products(self):
        if DEBUG:
            print(loop.run_until_complete(client.get_coinshop_products()))
        else:
            (loop.run_until_complete(client.get_coinshop_products()))

    def test_get_site_stats(self):
        if DEBUG:
            print(loop.run_until_complete(client.get_site_stats()))
        else:
            (loop.run_until_complete(client.get_site_stats()))

    def test_get_problem_by_id_array(self):
        for problem_id_array in problem_id_array_list:
            if DEBUG:
                print(loop.run_until_complete(client.get_problem_by_id_array(problem_id_array)))
            else:
                (loop.run_until_complete(client.get_problem_by_id_array(problem_id_array)))

    def test_get_problem_by_id(self):
        for problem_id in problem_id_list:
            if DEBUG:
                print(loop.run_until_complete(client.get_problem_by_id(problem_id)))
            else:
                (loop.run_until_complete(client.get_problem_by_id(problem_id)))

    def test_get_problem_level(self):
        if DEBUG:
            print(loop.run_until_complete(client.get_problem_level()))
        else:
            (loop.run_until_complete(client.get_problem_level()))

    def test_search_problem(self):
        for query, direction, page, sort in search_query_list:
            if DEBUG:
                print(loop.run_until_complete(client.search_problem(query, direction, page, sort)))
            else:
                print(loop.run_until_complete(client.search_problem(query, direction, page, sort)))

    def test_get_search_auto_completion(self):
        for query in query_list:
            if DEBUG:
                print(loop.run_until_complete(client.get_search_auto_completion(query)))
            else:
                (loop.run_until_complete(client.get_search_auto_completion(query)))


if __name__ == "__main__":
    unittest.main()
