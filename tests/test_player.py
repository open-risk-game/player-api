import os
import json
import pytest
import aiomysql
from player import Player

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = int(os.environ.get('DB_PORT'))
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')


@pytest.fixture
async def pool(loop):
    async with aiomysql.create_pool(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
            db=DB_NAME) as pool:
        yield pool


class FakeURL:

    def __init__(self):
        self.query = {'id': 1}


class FakeRequest:

    def __init__(self, _raise_exception=None, _json=None, app=None):
        self._json = _json
        self.app = app or {}
        self.rel_url = FakeURL()

    def json(self):
        if self._raise_exception:
            json.loads('None')
        return self._json


async def test_get_player(pool):
    request = FakeRequest(app={'pool': pool})
    response = await Player.get(request)
    actual = json.loads(response.text)
    expected = {
            'id': 1,
            'username': 'Billy-Bob'
            }
    assert expected == actual
