from flask import Blueprint
from controllers.products import list_sites_controller, list_products_controller, list_brands_controller, get_product_details_controller
# from middlewares.pagination import pagination_middleware
from flask import request

products_blueprint = Blueprint('products_blueprint', __name__)

@products_blueprint.get('/sites')
def list_site():
    # print(request.args.get("page"))
    return list_sites_controller(request)


@products_blueprint.get('/brands')
def list_brands():
    return list_brands_controller(request)


@products_blueprint.get('/products')
def list_products():
    return list_products_controller(request)

@products_blueprint.get('/products/<string:id>')
def get_product_details(id):
    return get_product_details_controller(id)