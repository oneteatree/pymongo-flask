from flask import Flask
from flask_pymongo import pymongo
from app import app


CONNECTION_STRING = "mongodb+srv://pyUse:161612@thepiecluster.p9dme.mongodb.net/thepiecluster?retryWrites=true&w=majority"


client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('thepiecluster')
user_collection = pymongo.collection.Collection(db, 'user_collection')