import os
import json
import pytest
import aiomysql
from player import Player


@pytest.fixture
async def pool():
    async with aiomysql.create_pool(
            host=os.environ.get('DB_HOST'),
            port=int(os.environ.get('DB_PORT')),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS'),
            db=os.environ.get('DB_NAME')) as pool:
        yield pool


class FakeRequest():

    def __init__(self, _raise_exception=None, _json=None, app=None):
        self._json = _json
        self.app = app or {}

    def json(self):
        if self._raise_exception:
            json.loads('None')
        return self._json


@pytest.mark.asyncio
async def test_create(pool):
    fake_request = FakeRequest(app={'pool': pool})
    player = Player('1')
    actual = await player.create(fake_request)
    expected = {'error': 'player no created'}
    assert expected == actual
