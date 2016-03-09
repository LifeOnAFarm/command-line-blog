import pymongo

"""
    Description:    Database that the program will use with MongoDB
"""

__author__ = "Seamus de Cleir"


class Database(object):
    # URI default that mongo uses
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    # Sets the dbs that mongo uses to fullstack
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["fullstack"]

    @staticmethod
    def insert(collection, query):
        Database.DATABASE[collection].insert(query)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)