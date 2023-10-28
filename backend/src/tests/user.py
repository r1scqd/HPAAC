import unittest

import requests

base_url = "http://127.0.0.1:8080/api"


class BaseTest(unittest.TestCase):
    def test_get(self):
        requests.get(base_url)

    def test_post(self):
        pass

    def test_delete(self):
        pass


if __name__ == '__main__':
    unittest.main()
