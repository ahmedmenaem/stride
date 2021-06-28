from json import dumps
from utils.db import db
from flask import jsonify
from utils.paging import get_pagination
from bson.objectid import ObjectId


def list_sites_controller(request):
    limit, offset, page = get_pagination(request.args.get("page"))
    sites = []
    for s in db.sites.find().skip(offset).limit(limit):
        sites.append({"name": s["name"], "id": str(s["_id"])})
    docs_size = db.sites.count_documents()
    return jsonify({
        'data' : sites,
        "success": True,
        "message": "",
        "page": page,
        "total": (docs_size // limit)
    })

def list_brands_controller(request):
    limit, offset, page = get_pagination(request.args.get("page"))
    brands = []
    for s in db.brands.find().skip(offset).limit(limit):
        brands.append({"name": s["name"], "id": str(s["_id"])})
    docs_size = db.brands.count_documents()
    return jsonify({
        'data' : brands,
        "success": True,
        "message": "",
        "page": page,
        "total": (docs_size // limit)
    })

def list_products_controller(request):
    limit, offset, page = get_pagination(request.args.get("page"))
    products = []
    filter_dict = {}
    if request.args.get("brand"):
        filter_dict["brand"] = request.args.get("brand")
    for s in db.products.find(filter_dict).skip(offset).limit(limit):
        products.append({"name": s["name"], "id": str(s["_id"]), "brand": s["brand"]})
    docs_size = db.products.count_documents(filter_dict)
    return jsonify({
        'data' : products,
        "success": True,
        "message": "",
        "size": str(docs_size),
        "page": page,
        "total": (docs_size // limit)
    })

def get_product_details_controller(id):
    product = db.products.find_one({"_id": ObjectId(id)})
    if product:
        data = {
            "id": str(product["_id"]),
            "brand": product["brand"], 
            "name": product["name"],
            "price": product["price"],
            "sizes": product["sizes"],
            "links": product["links"]
        }
        return jsonify({
            "data": [data],
            "success": True,
            "message": ""
        })
    else:
        return jsonify({
            "data": [],
            "success": True,
            "message": ""
        })