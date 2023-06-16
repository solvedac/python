import solvedac_community as SolvedAC
import asyncio
import unittest
import os

loop = asyncio.get_event_loop()
TOKEN = os.environ["SolvedAC"]
client = SolvedAC.Client(solvedac_token=TOKEN)


class Test(unittest.TestCase):
    def test_verity_account_credentials(self):
        print(loop.run_until_complete(client.verify_account_credentials()))


if __name__ == "__main__":
    unittest.main()
