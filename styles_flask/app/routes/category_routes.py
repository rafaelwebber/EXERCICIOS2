from flask import Blueprint, blueprints, jsonify, request
from pydantic import ValidationError
category_bp = Blueprint('category_bp', __name__)



@category_bp.route('/category', methods=['GET'])
def get_category():
    return jsonify({"mensagem":"Está é a rota get de category"})

@category_bp.route('/category', methods=['POST'] )
def create_category():
    return jsonify({"mensagem":"Está é a rota de criação de category"})
    

@category_bp.route('/category', methods=['PUT'])
def update_category():
    return jsonify({"mensagem":"Está é a rota de atualização de category"})

@category_bp.route('/category', methods=['DELETE'])
def delete_category():
    return jsonify({"mensgaem":"Está é a rota de deleção de category"})