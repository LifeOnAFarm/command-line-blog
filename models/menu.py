from database import Database
from models.blog import Blog
__author__ = "Seamus de Cleir"


class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}!".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one("blogs", {"author": self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog["id"])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title:")
        description = input("Enter blog description:")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        r_or_w = input("Do you want to Read (R) or Write (W)?")

        if r_or_w == "R":
            self._list_blogs()
            self._view_blog()
        elif r_or_w == "W":
            self.user_blog.new_post()
        else:
            print("Please try again")

    @staticmethod
    def _list_blogs():
        blogs = Database.find(collection="blogs",
                              query={})

        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog["id"], blog["title"], blog["author"]))

    @staticmethod
    def _view_blog():
        blog_to_see = input("Enter ID of the blog you want to see:")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Date: {}, Title: {},\n\n Content: {}".format(post["created_date"], post["title"], post["content"]))