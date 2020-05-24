import aiomysql
from aiohttp import web


class Player:

    def __init__(self, username):
        self.username = username

    async def create(self, request):

        async with request.app['pool'].acquire() as db_conn:
            cursor = await db_conn.cursor(aiomysql.DictCursor)
            query = f'''
            INSERT INTO players ()
            VALUES ({self.username})
            '''
            if await cursor.execute(query) == 0:
                response = {'error': 'player not created'}
                return web.Response(response)
            await db_conn.commit()
        return web.Response(text='Player created')

    async def get(request):
        return web.json_response(Player('abc').__dict__)
