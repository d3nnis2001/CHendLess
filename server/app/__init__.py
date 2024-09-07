from flask import Flask
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from pymongo import MongoClient

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "fa18f2203a90b7fc58d1cbfdb97464893adf071d782bf740cacca133796a04a9"
    app.config['JWT_SECRET_KEY'] = '625f4950f37073af999b38a7a57d25745bed6748948d9fcfa3ebf4c902b7c3ed'
    
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    client = MongoClient('localhost', 27017)
    app.db = client['ChendLess']
    
    CORS(app)

    from .controller.user_controller import user_bp
    app.register_blueprint(user_bp)

    return app
