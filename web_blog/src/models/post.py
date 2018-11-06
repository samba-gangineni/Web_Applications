import uuid
from .database import Database
from datetime import datetime as dt

__author__ = 'Sambasiva Rao Gangineni'

class Post(object):
    
    #Properties each post have
    def __init__(self,blog_id, title,content,author, created_date = dt.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self._id = uuid.uuid4().hex if _id is None else _id
        self.created_date = created_date

    #Saving the post to database 
    def save_to_mongo(self):
        Database.insert(collection = 'posts', data = self.json())

    #This creates the json represntaiton of the post
    def json(self):
        return {
            '_id':self._id,
            'blog_id':self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'title':self.title,
            'created_date' : self.created_date
        }

    @classmethod
    def from_mongo(cls , id):
        post_data = Database.find_one(collection='posts',query={'id':id})
        return cls(**post_data)
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts',query={'blog_id':id})]