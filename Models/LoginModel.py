import pymongo
import bcrypt
from pymongo import MongoClient


class LoginModel:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.pytests
        self.users = self.db.users

    def check_user(self, data):
        user = self.users.find_one({'username': data.username})

        if user:
            if bcrypt.checkpw(data.password.encode(), user['password']):
                return user
            else:
                return False
        else:
            return False

    def update_info(self, data):
        updated = self.users.update_one({
            'username': data['username']
        }, {'$set': data})

        return True

    def get_profile(self, user):
        user_info = self.users.find_one({'username': user})
        return user_info

    def update_image(self, update):
        updated = self.users.update_one({'username': update['username']}, {'$set': {update['type']: update['img']}})
        return updated
