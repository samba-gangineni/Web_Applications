from database import Database
from models.post import Post

__author__ = "Sambasiva Rao Gangineni"

Database.initialize()

post = Post("Post1 title", "Post1 Content", "Post1 author")
post2 = Post("Post2 title", "Post2 Content", "Post2 author")
