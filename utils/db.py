from config.mongo import MONGODB_URL
from pymongo import MongoClient

Client = MongoClient(MONGODB_URL)
db = Client['strid_db']
