from decouple import config
from pymongo import MongoClient


db_client = MongoClient(config('ENGINE_CONN')).kc_feb_23