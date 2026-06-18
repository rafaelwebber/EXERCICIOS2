from flask import Blueprint, jsonify, request
from app.models.user import LoginPayload
main_bp = Blueprint('main_bp', __name__)
from pydantic import ValidationError
from app import db
from bson import ObjectId



#RF: O sistema deve permitir que um usuario se autentique para obter um token

@main_bp.route('/login', methods=['POST'])
def login():
    try:
        raw_data = request.get_json()
        user_data = LoginPayload(**raw_data)
    
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        jsonify({"error": "Erro durante a requisição do dado"}), 500

    if user_data.username == 'admin' and user_data.password == '123':
        return jsonify({"mensage": "Login bem sucedido!"})

    else:
        return jsonify({"mensage": "Credenciais Invalidas!"})
    
    return jsonify({"mensagem": f"Realizar login do usuario {user_data.model_dump_json}"})

#RF: O sistema deve permitir a listagem de todos os produtos
@main_bp.route('/products', methods=['GET'])
def get_products():
    products_cursor = db.products.find({})
    products_list = []
    for products in products_cursor:
        products['_id'] = str(products['_id'])
        products_list.append(products)
    return jsonify(products_list)


#RF: O sistema deve permitir a criaação de um novo produto
@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({"mensagem":"Esta é a rota de criação de produto"})

#RF: O sistema deve permitir a visualização dos detalhes de um unico produto
@main_bp.route('/products/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        oid = ObjectId(product_id)
    except Exception as e:
        return jsonify({"error":f"erro ao buscar o produto {product_id}: {e}"})

    product = db.products.find_one({'_id':oid})

    if product:
        product['_id'] = str(product['_id'])
        return jsonify(product)

    else:
        return jsonify({"error":f"Produto com o id: {product_id} - Não encontrado"})

#RF: O sistema deve permitir a atualização de um unico produto e prduto existente
@main_bp.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return jsonify({"mensagem":f"Esta é a rota de atualização do produto com o id {product_id}"})

#RF: O sistema deve permitir a deleção de um unico produto e produto existente
@main_bp.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return jsonify({"mensagem":f"Esta é uma mensagem de deleção do produto com o id {product_id}"})

#RF: O sistema deve permitir a importação de vendas atraves de um arquivo
@main_bp.route('/sales/upload', methods=['POST'])
def update_sales():
    return jsonify({"mensagem":f"Esta é a rota de upload do arquivo de vendas"})

@main_bp.route('/')
def index():
    return jsonify({"mensagem":"Bem vindo"})



