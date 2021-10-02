import json
from utils import logger
from connection import return_connection


def lambda_handler():
    connection = return_connection()
    with connection.cursor() as cur:
        cur.execute(
            f"select id, name, movie_id from lecket.movie where name like '%{target}%'"
        )
        result = [{
            'id': row[0],
            'name': row[1],
            'movie_id': row[2]
        } for row in cur]
        logger.info(result)
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }