import solvedac_community as SolvedAC
import asyncio
import unittest
import os

loop = asyncio.get_event_loop()
TOKEN1 = os.environ["SolvedAC1"]
TOKEN2 = os.environ["SolvedAC2"]

client1 = SolvedAC.Client(solvedac_token=TOKEN1)
client2 = SolvedAC.Client(solvedac_token=TOKEN2)


class Test(unittest.TestCase):
    def test_verity_account_credentials(self):
        print(loop.run_until_complete(client1.verify_account_credentials()))
        print(loop.run_until_complete(client2.verify_account_credentials()))


if __name__ == "__main__":
    unittest.main()
