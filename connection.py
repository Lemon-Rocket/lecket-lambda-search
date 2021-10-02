import os
import sys
from utils import logger
import pymysql


def return_connection():
    try:
        connection = pymysql.connect(
            host=os.getenv('LECKET_HOST', '30.40.0.10:3307'),
            user=os.getenv('LECKET_USERNAME', 'admin'),
            passwd=os.getenv('LECKET_PASSWORD', 'password'),
            db=os.getenv('LECKET_DB', 'lecket'),
            connect_timeout=5
        )
        return connection
    except pymysql.MySQLError as e:
        logger.error(
            "ERROR: Unexpected error: Could not connect to MySQL instance."
        )
        logger.error(f'{e}')
        sys.exit()
