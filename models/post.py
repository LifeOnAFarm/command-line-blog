from database import Database
import uuid
import datetime

"""
    Description: Post class for interacting with MongoDB
"""

__author__ = "Seamus de Cleir"


class Post(object):

    def __init__(self, title, content, author, blog_id, created_date=datetime.datetime.utcnow(), post_id=None):
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        self.created_date = created_date

        # Sets a random hex value as the post_id if the post_id is empty
        self.post_id = uuid.uuid4().hex if post_id is None else post_id

    # Posts to post Database
    def save_to_mongo(self):
        Database.insert(collection="post", query=self.json())

    def json(self):
        return {
            "id": self.post_id,
            "blog_id": self.blog_id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "created_date": self.created_date
        }

    # Find a post by id
    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection="posts", query={"id": id})

    # Finds many posts by id
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection="posts", query={"blog_id": id})]
