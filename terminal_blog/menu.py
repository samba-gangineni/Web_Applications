from database import Database
from models.blog import Blog
class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()
        
    def _user_has_account(self):
        blog =  Database.find_one('blogs',{'author':self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False
        
    def _prompt_user_for_account(self):
        title = input("Enter the blog title: ")
        description = input("Write the description: ")
        blog = Blog(author = self.user,
                    title = title,
                    description = description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        query = input("Do you want to read(R) or write(W) blogs? ")
        if query=='R':
            self._list_blogs()
            self._view_blog()
        elif query=='W':
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")
    
    def _list_blogs(self):
        blogs = Database.find(collection='blogs',query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'],blog['title'],blog['author']))

    def _view_blog(self):
        blog_required = input("Please enter the id of the required blog: ")
        blog = Blog.from_mongo(blog_required)
        posts = blog.get_posts()

        for post in posts:
            print("Date {}, title:{} \n\n{}".format(post['created_date'],post['title'],post['content']))
