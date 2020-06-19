import os
import aiomysql
from aiohttp import web
from player import Player

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = int(os.environ.get('DB_PORT'))


async def create_db_pool(app):
    app['pool'] = await aiomysql.create_pool(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            db=DB_NAME,
            port=DB_PORT
        )

app = web.Application()

app.on_startup.append(create_db_pool)

app.add_routes([
        web.post('/v0/player/create', Player.create),
        web.get('/v0/player', Player.get)
        ])

if __name__ == "__main__":
    web.run_app(app)
