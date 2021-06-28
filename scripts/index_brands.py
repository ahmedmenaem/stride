from parse_data import get_brands
from db import db

def index_brands(site = 'zalando'):
    cleaned_brands = []
    for site in db.sites.find({ "name": site }):
        for brands in get_brands():
            cleaned_brands = list(set(cleaned_brands + brands))
            print(cleaned_brands)
    brands_documents = list(map(lambda b: { "name": b, "siteId": site["_id"] }, cleaned_brands))
    result = db.brands.insert_many(brands_documents)
    print("brands saved to db")

if __name__ == "__main__":
    index_brands()