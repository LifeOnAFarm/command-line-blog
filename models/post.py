from database import Database
import uuid
import datetime

"""
    Description: Post class for interacting with MongoDB
"""

__author__ = "Seamus de Cleir"


class Post(object):

    def __init__(self, title, content, author, blog_id, created_date=datetime.datetime.utcnow(), id=None):
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        self.created_date = created_date

        # Sets a random hex value as the id if the id is empty
        self.id = uuid.uuid4().hex if id is None else id

    # Posts to post Database
    def save_to_mongo(self):
        Database.insert(collection="post", query=self.json())

    def json(self):
        return {
            "id": self.id,
            "blog_id": self.blog_id,
            "author": self.author,
            "title": self.title,
            "content": self.content,
            "created_date": self.created_date
        }

    # Find a post by id
    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection="posts", query={"id": id})

        return Post(blog_id=post_data["blog_id"],
                    title=post_data["title"],
                    content=post_data["content"],
                    author=post_data["author"],
                    created_date=post_data["created_date"],
                    id=post_data["id"])

    # Finds many posts by id
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection="posts", query={"blog_id": id})]
