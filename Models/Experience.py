import pymongo
import bcrypt
from pymongo import MongoClient


class Experience:

	def __init__(self):
		self.client = MongoClient()
		self.db = self.client.pytests
		self.users = self.db.users
		self.exper = self.db.experience

	def inser_exper(self, data):
		insertexper = self.exper.insert({'username': data.username,'exper_name': data.exper_name, 'content': data.exper_content})
		return True

	def get_all_expers(self):
		all_expers = self.exper.find()
		new_expers = []
		for exper in all_expers:
			exper['user'] = self.users.find_one({'username': exper['username']})
			new_expers.append(exper)

		return new_expers