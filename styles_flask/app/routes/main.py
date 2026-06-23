from flask import Blueprint, current_app, jsonify, request
from werkzeug.security import check_password_hash
from app.models.user import LoginPayload
main_bp = Blueprint('main_bp', __name__)
from pydantic import ValidationError
from app import db
from bson import ObjectId
from app.models.products import *
from app.decorators import token_required
from datetime import datetime, timedelta, timezone
import jwt


def normalize_product_document(product: dict) -> dict:
    normalized = dict(product)
    # Compatibilidade com registros antigos gravados com chave incorreta.
    if 'stock' not in normalized and 'stok' in normalized:
        normalized['stock'] = normalized['stok']
    # Evita 500 em registros legados sem SKU.
    if 'sku' not in normalized:
        normalized['sku'] = 'SEM-SKU'
    return normalized
#RF: O sistema deve permitir que um usuario se autentique para obter um token

@main_bp.route('/login', methods=['POST'])
def login():
    try:
        raw_data = request.get_json()
        user_data = LoginPayload(**raw_data)
    
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception:
        jsonify({"error": "Erro durante a requisição do dado"}), 500

    user = db.user.find_one({"username": user_data.username})
    if user and check_password_hash(user["password_hash"], user_data.password):
        token = jwt.encode(
            {
                "user_id": user_data.username,
                "username": user["username"],
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
            },
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )

        return jsonify({'access_token': token}), 200

    return jsonify({"mensage": "Credenciais Invalidas!"}), 401
    


#RF: O sistema deve permitir a listagem de todos os produtos
@main_bp.route('/products', methods=['GET'])
def get_products():
    products_cursor = db.products.find({})
    products_list = [
        ProductDBMondel(**normalize_product_document(product)).model_dump(by_alias=True, exclude_none=True)
        for product in products_cursor
    ]
    return jsonify(products_list)


#RF: O sistema deve permitir a criaação de um novo produto
@main_bp.route('/products', methods=['POST'])
@token_required
def create_product(token):
    try:
        payload = request.get_json(silent=True)
        if not payload:
            return jsonify({"error": "Corpo da requisição JSON é obrigatório"}), 400

        product = Product(**payload)

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    result = db.products.insert_one(product.model_dump())
    return jsonify({"mensagem":"Esta é a rota de criação de produto",
                "id": str(result.inserted_id)}), 201

#RF: O sistema deve permitir a visualização dos detalhes de um unico produto
@main_bp.route('/products/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        oid = ObjectId(product_id)
    except Exception as e:
        return jsonify({"error":f"erro ao buscar o produto {product_id}: {e}"})

    product = db.products.find_one({'_id':oid})

    if product:
        product_model = ProductDBMondel(**normalize_product_document(product)).model_dump(by_alias=True, exclude_none=True)
        return jsonify(product_model)

    else:
        return jsonify({"error":f"Produto com o id: {product_id} - Não encontrado"})

#RF: O sistema deve permitir a atualização de um unico produto e prduto existente
@main_bp.route('/product/<string:product_id>', methods=['PUT'])
@token_required
def update_product(token, product_id):
    try:
        oid = ObjectId(product_id)
        update_data = UpdateProduct(**request.get_json())
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    

    update_result = db.products.update_one(
        {"_id": oid},
        {"$set": update_data.model_dump(exclude_unset=True)}
    )

    if update_result.matched_count == 0:
        return jsonify({"error":"Produto não ncontrado" }), 404


    updated_product = db.products.find_one({"_id": oid}) 
    return jsonify(
        ProductDBMondel(**normalize_product_document(updated_product)).model_dump(by_alias=True, exclude_none=True)
    )

#RF: O sistema deve permitir a deleção de um unico produto e produto existente
@main_bp.route('/product/<string:product_id>', methods=['DELETE'])
@token_required
def delete_product(token, product_id):
    try: 
        oid = ObjectId(product_id)
    except Exception:
        return jsonify({"error":"id do produto invalido"}), 400

    delete_result = db.products.delete_one({"_id": oid})

    if delete_result.deleted_count == 0:
        return jsonify({"error": "Porduto não foi encontrado"}), 404


    return "", 204

#RF: O sistema deve permitir a importação de vendas atraves de um arquivo
@main_bp.route('/sales/upload', methods=['POST'])
def update_sales():
    return jsonify({"mensagem":f"Esta é a rota de upload do arquivo de vendas"})


@main_bp.route('/')
def index():
    return jsonify({"mensagem":"Bem vindo"})



