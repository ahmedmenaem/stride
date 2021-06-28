from db import db


def index_sites():
    craweled_sites = ["omoda", "zalando", "ziengs"]
    sites_documents = list(map(lambda x: { "name": x } ,craweled_sites))
    sites = db.sites
    result = sites.insert_many(sites_documents)
    print("sites save to db")

if __name__ == "__main__":
    index_sites()
