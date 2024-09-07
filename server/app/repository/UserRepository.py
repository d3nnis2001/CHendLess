from flask import current_app

class UserRepository:
    def __init__(self):
        self.collection = current_app.db['users']

    def find_by_username(self, username):
        return self.collection.find_one({'username': username})

    def create(self, user):
        return self.collection.insert_one({
            'username': user.username,
            'password': user.password
        })