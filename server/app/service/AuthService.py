from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from ..model.User import User

bcrypt = Bcrypt()

class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register(self, username, password):
        existing_user = self.user_repository.find_by_username(username)
        if existing_user:
            return False, "Benutzername bereits vergeben"
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username, hashed_password)
        self.user_repository.create(new_user)
        return True, "Benutzer erfolgreich registriert"

    def login(self, username, password):
        user = self.user_repository.find_by_username(username)
        if user and bcrypt.check_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['_id']))
            return True, access_token
        return False, "Ungültige Anmeldeinformationen"
