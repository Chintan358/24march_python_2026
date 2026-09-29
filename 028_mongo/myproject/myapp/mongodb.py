
from pymongo import MongoClient

url = "mongodb+srv://chintantops_db_user:test@cluster0.sor54ut.mongodb.net/?appName=Cluster0"
client = MongoClient(url)

db = client["tops"]

students_collection = db["student"]
category_collection = db['Category']
