import pymongo
import bcrypt
from pymongo import MongoClient
import datetime
import humanize
from bson import ObjectId  # for returning comment as a json


class Posts:

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.pytests
        self.users = self.db.users
        self.posts = self.db.posts
        self.comments = self.db.comment

    def inser_post(self, data):
        insertpost = self.posts.insert(
            {'username': data.username, 'content': data.content, 'date_added': datetime.datetime.now()})
        return True

    def get_all_posts(self):
        all_posts = self.posts.find().sort('date_added', -1)
        new_posts = []
        for post in all_posts:
            post['user'] = self.users.find_one({'username': post['username']})  # find just one
            post['timestamp'] = humanize.naturalday(datetime.datetime.now() - post[
                'date_added'])  # if it is key error, mean some table doens't have that data
            post['old_comment'] = self.comments.find({'post_id': str(post['_id'])})  # find all

            post['comment'] = []

            for comment in post['old_comment']:
                comment['user'] = self.users.find_one({'username': comment['username']})
                comment['time'] = humanize.naturalday(datetime.datetime.now() - comment['date_added'])
                post['comment'].append(comment)

            new_posts.append(post)

        return new_posts

    def get_user_posts(self, user):
        all_posts = self.posts.find({'username': user}).sort('date_added', -1)
        new_posts = []
        for post in all_posts:
            post['user'] = self.users.find_one({'username': post['username']})
            new_posts.append(post)

        return new_posts

    def add_comment(self, comment):
        insert_comment = self.comments.insert(
            {'post_id': comment['post_id'], 'username': comment['username'], 'content': comment['content'],
             'date_added': datetime.datetime.now()})
        return insert_comment

    def delete_post(self, data):
        delete = data.post_id
        Ob = ObjectId(delete)
        result = self.posts.delete_one({'_id': Ob})
        print(delete)
        return result
