import json
import os
import sys

from bson.json_util import dumps

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

import mongodb_client

NEWS_TABLE_NAME = "news"

def getOneNews():
    db = mongodb_client.get_db()
    news = db[NEWS_TABLE_NAME].find_one()
    return json.loads(dumps(news))
