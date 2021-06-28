import os

MONGODB_HOST = os.getenv("MONGODB_HOST") or "localhost"
MONGODB_PORT = os.getenv("MONGODB_PORT") or int("27017")
MONGODB_NAME = os.getenv("MONGODB_NAME") or "strid_db"

MONGODB_URL = "mongodb://{host}:{port}/{db}".format(host=MONGODB_HOST, port=MONGODB_PORT, db=MONGODB_NAME)
