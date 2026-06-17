from flask import Blueprint, jsonify, request
from app.models.user import LoginPayload
main_bp = Blueprint('main_bp', __name__)
from pydantic import ValidationError



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
@main_bp.route('/products')
def get_products():
    return jsonify({"mensagem":"Esta é a rota de listagem dos produtos"})


#RF: O sistema deve permitir a criaação de um novo produto
@main_bp.route('/products', methods=['POST'])
def create_product():
    return jsonify({"mensagem":"Esta é a rota de criação de produto"})

#RF: O sistema deve permitir a visualização dos detalhes de um unico produto
@main_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return jsonify({"mensagem":f"Esta é a rota de visualização do detalhe do id do produto {product_id}"})

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



