import pymongo
from pymongo import MongoClient
import bcrypt  # checking password


class RegisterModel:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.pytests
        self.users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        id = self.users.insert_one(
            {'username': data.username, 'name': data.name, 'email': data.email, 'password': hashed, 'avater': "",
             "background": "", 'about': "", 'birthday': ''})
        print('Data id is', data.password)
        print('Data id is', id)
        myuser = self.users.find_one({'username': data.username})

        print(myuser['password'])
        print('password'.encode())
        if bcrypt.checkpw('password'.encode(), myuser['password']):  # check if they are matches
            print("It Matches!")
        else:
            print('Unmatch')
