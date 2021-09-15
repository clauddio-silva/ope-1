from flask_restx import Resource, Namespace
from flask import request, jsonify, make_response
from src.domain.dto import Product as ProductDto
from src.main.adapters import flask_adapter

from src.main.compose import create_product_composer
from src.main.compose import list_products_composer

product_namespace = Namespace('products')
product = product_namespace.model('Product', ProductDto)


@product_namespace.route('/')
class Products(Resource):
    @product_namespace.expect(product)
    @product_namespace.doc(responses={201: 'Created',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def post(self):
        response = flask_adapter(request, create_product_composer())
        return make_response(jsonify(response), int(response['status']))

    @product_namespace.doc(responses={200: 'OK',
                                   400: 'Bad Request',
                                   409: "Integrity Error",
                                   500: "Internal Server Error"})
    def get(self):
        response = flask_adapter(request, list_products_composer())
        return make_response(jsonify(response), int(response["status"]))