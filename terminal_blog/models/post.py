import uuid
from database import Database

__author__ = 'Sambasiva Rao Gangineni'

class Post(object):
    
    #Properties each post have
    def __init__(self,blog_id, title,content,author, date = today, id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id
        self.created_date = date

    #Saving the post to database 
    def save_to_mongo(self):
        Database.insert(collection = 'posts', data = self.json())

    #This creates the json represntaiton of the post
    def json(self):
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'author' : self.author,
            'content' : self.content,
            'title':self.title,
            'created_date' : self.created_date
        }

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts',query={'id':id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts',query={'id':id})]