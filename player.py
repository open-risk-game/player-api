import aiomysql
from aiohttp import web


class Player:

    def __init__(self, username):
        self.username = username

    def create(self, request):

        async with request.app['pool'].aqcuire() as db_conn:
            cursor = await db_conn.cursor(aiomysql.DictCursor)
            query = '''
            INSERT INTO players ()
            VALUES ()
            '''
            if await cursor.exectue(query) == 0:
                response = {'error': 'player not created'}
                return web.json_response(response)
            await db_conn.commit()
        return web.Response(text='Player created')

    async def get(request):
        return web.json_response(Player('abc').__dict__)
