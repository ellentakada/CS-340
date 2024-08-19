from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user=None, password=None, host=None, port=None, db=None, col=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        
        USER = user
        PASS = password
        HOST = host
        PORT = port
        DB = db
        COL = col

        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            cursor = self.collection.find(data)
            return list(cursor)
        else:
            raise Exception("Nothing to query, because data parameter is empty")
            return False
       
# Create method to implement the U in CRUD.
    def update(self, data, update):
        if data is not None:
            result = self.collection.update_many(data, {'$set': update})
            return result.modified_count
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            
# Create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            delete = self.collection.find(data).count()
            if self.collection.find(data).count() > 1:
                self.collection.delete_many(data)
            else:
                self.collection.delete_one(data)
            return delete
        else:
            raise Exception("Nothing to delete, because data parameter is empty")