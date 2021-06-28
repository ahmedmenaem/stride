from db import db
from parse_data import get_products

def index_products():
    print("saving products...")
    for products_documents in get_products():
        products = db.products
        result = products.insert_many(products_documents)
        print("products save to db")

if __name__ == "__main__":
    index_products()