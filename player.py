import aiomysql
from aiohttp import web


class Player:

    def __init__(self, username):
        self.username = username

    async def create(request):

        async with request.app['pool'].acquire() as db_conn:
            data = await request.json()
            name = data['username']
            cursor = await db_conn.cursor(aiomysql.DictCursor)
            query = f'''
            INSERT INTO players (username) VALUES ("{name}")
            '''
            await cursor.execute(query)
            await db_conn.commit()
        return web.Response(text='Player created')

    async def get(request):
        player_id = request.rel_url.query['id']
        async with request.app['pool'].acquire() as db_conn:
            cursor = await db_conn.cursor(aiomysql.DictCursor)
            query = f'''
            SELECT *
            FROM players
            WHERE id = {player_id}
            '''
        await cursor.execute(query)
        x = await cursor.fetchone()
        data = {
                'id': x['id'],
                'username': x['username']
                }
        return web.json_response(data)
