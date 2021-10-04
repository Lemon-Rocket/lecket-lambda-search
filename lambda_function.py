import json
from utils import logger
from connection import return_connection


def lambda_handler(event, context):
    target = event.get(
        'queryStringParameters', {}
    ).get('target')
    connection = return_connection()
    with connection.cursor() as cur:
        cur.execute(
            f"select id, name, movie_id from lecket.movie where name like '%{target}%' order by name ASC limit 10"
        )
        result = [{
            'id': row[0],
            'name': row[1],
            'movieId': row[2]
        } for row in cur]
        logger.info(result)
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(result)
    }
