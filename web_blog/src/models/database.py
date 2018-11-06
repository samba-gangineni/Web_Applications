import pymongo

__author__ = "Sambasiva Rao Gangineni"


# Inheriting the methods that object have
class Database(object):
    #The static variables as there is only one database.
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client  = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['samba']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
