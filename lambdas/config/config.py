import os
import logging


CONNECTION_KEY = {
    "host": os.environ.get('MONGO_HOST', 'mongo.dev.shiftpixy.com'),
    "port": os.environ.get('MONGO_PORT', 27017),
    "username": os.environ.get('MONGO_USERNAME', 'root'),
    "password": os.environ.get('MONGO_PASSWORD', 'password'),
    "authSource": os.environ.get('MONGO_AUTH_SOURCE', 'admin'),
    "db_name": os.environ.get('MONGO_DB_NAME', 'recommendation_engine')
}


MAPBOX_TOKEN = {
    "mapbox_token": os.environ.get('MAPBOX_TOKEN', 'pk.eyJ1Ijoic3lzb3BzLXNoaWZ0cGl4eSIsImEiOiJjanI4N29nZmUwMDBjNDludnQ5\
a21wYTU2In0.J2LISQd3x_iqPCS3hG7dbw')
}

DAL_URL = {
    "base_url": os.environ.get(
        'DAL_URL', 'http://dal.dev.shiftpixy.com/api/re'),
    "token": os.environ.get('TOKEN', 'token')
}

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')

logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)
