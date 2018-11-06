import uuid
from common.database import Database
from datetime import datetime as dt

__author__ = 'Sambasiva Rao Gangineni'

class Post(object):
    
    #Properties each post have
    def __init__(self,blog_id, title,content,author, date = dt.utcnow(), id=None):
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

    @classmethod
    def from_mongo(cls , id):
        post_data = Database.find_one(collection='posts',query={'id':id})
        return cls(blog_id = post_data['blog_id'], 
                    title = post_data['title'],
                    content=post_data['content'],
                    author=post_data['author'], 
                    date = post_data['date'], 
                    id=post_data['id'])
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts',query={'blog_id':id})]