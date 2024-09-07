# user_controller.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..service.AuthService import AuthService
from ..repository.UserRepository import UserRepository

user_bp = Blueprint('user', __name__, url_prefix='/api/user')

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    auth_service = AuthService(UserRepository())
    success, message = auth_service.register(username, password)
    
    if success:
        return jsonify({"message": message}), 201
    return jsonify({"error": message}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    auth_service = AuthService(UserRepository())
    success, result = auth_service.login(username, password)
    
    if success:
        return jsonify({"access_token": result}), 200
    return jsonify({"error": result}), 401

@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200