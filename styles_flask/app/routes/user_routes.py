from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from app import db
user_bp = Blueprint('user_bp', __name__)
from app.models.user import *
from werkzeug.security import generate_password_hash
from app.decorators import token_required




def build_validation_error_response(error: ValidationError):
    errors = error.errors()
    missing_fields = []

    for item in errors:
        if item.get("type") == "missing":
            loc = item.get("loc", [])
            if loc:
                missing_fields.append(str(loc[-1]))

    if missing_fields:
        return jsonify({
            "error": "Campos obrigatórios ausentes",
            "missing_fields": sorted(set(missing_fields)),
            "details": errors
        }), 400

    return jsonify({"error": errors}), 400

@user_bp.route('/user', methods=['GET'])
@token_required
def list_user(token):
    user_cursor = db.user.find({})
    user_list = []

    for user in user_cursor:
        try:
            user_public = UserPublic(**user)
            user_list.append(
                user_public.model_dump(
                    mode="json",
                    by_alias=True,
                    exclude_none=True
                )
            )
        except ValidationError:
            continue

    return jsonify(user_list)

@user_bp.route('/user', methods=['POST'])
def create_user():
    try:
        payload = request.get_json(silent=True)
        if not payload or not isinstance(payload, dict):
            return jsonify({"error": "Corpo da requisição JSON é obrigatório"}), 400
        
        user = UserCreate(**payload)
        doc = user.model_dump(exclude={"password", "id"})
        doc["password_hash"] = generate_password_hash(user.password.get_secret_value())

    except ValidationError as e:
        return build_validation_error_response(e)
    except Exception:
        return jsonify({"error": "Erro interno ao criar usuário"}), 500

    result = db.user.insert_one(doc)
    return jsonify({"mensagem": "Sucesso", 
            "id": str(result.inserted_id)}), 201

@user_bp.route('/user/<string:user_id>', methods=['DELETE'])
@token_required
def delete_user(token, user_id):
    try:
        oid = ObjectId(user_id)
    
    except Exception:
        return jsonify({"erro": "ID invalido!"}), 400

    delete_result = db.user.delete_one({"_id": oid})

    if delete_result.deleted_count == 0:
        return jsonify({"error": "Usuario nao foi encontrado"}), 404

    return "", 204


