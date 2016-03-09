import uuid
import datetime
from database import Database
from models.post import Post

__author__ = "Seamus de Cleir"


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title:")
        content = input("Enter content:")
        date = datetime.datetime.utcnow()
        post = Post(author=self.author,
                    blog_id=self.id,
                    content=content,
                    title=title,
                    created_date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection="blogs",
                        query=self.json())

    def json(self):
        return {
            "id": self.id,
            "author": self.author,
            "title": self.title,
            "description": self.description
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection="blogs",
                                      query={"id": id})

        return cls(author=blog_data["author"],
                   title=blog_data["title"],
                   description=blog_data["description"],
                   id=blog_data["id"])
