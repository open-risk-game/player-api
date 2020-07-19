import json
import aiomysql
from aiohttp import web


class Player:

    def __init__(self, username):
        self.username = username

    @staticmethod
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

    @staticmethod
    async def get(request):
        player_id = request.rel_url.query['id']
        async with request.app['pool'].acquire() as db_conn:
            query = f'SELECT * FROM players WHERE id = {player_id}'
            cursor = await db_conn.cursor(aiomysql.DictCursor)
            await cursor.execute(query)
            result = await cursor.fetchone()
            if result is None:
                return web.json_response(
                        {'Error': f'No player found with id: {player_id}'}
                        )
        data = {
                'id': result['id'],
                'username': result['username']
                }
        return web.json_response(data)


async def get_on_board(request):
    params = request.rel_url.query
    board_id = params['id']
    async with request.app['pool'].acquire() as db_conn:
        query = f'''
            SELECT player.id, username, wins, draws, losses
            FROM player
            INNER JOIN game ON 
                game.player_id = player.id 
                AND game.board_id = {board_id}
        '''
        cursor = await db_conn.cursor(aiomysql.DictCursor)
        await cursor.execute(query)
        result = await cursor.fetchall()
        if result is None:
            return web.json_response(
                    {'Error': f'No player found on board {board_id}'}
                    )
    players = []
    for player in result:
        p = {
                "id": player.get('id'),
                "username": player.get('username')
                }
        players.append(p)
    return web.json_response(players)
