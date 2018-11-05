__author__ = "Sambasiva Rao Gangineni"

import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['samba']
collection = database['students']

students = [student['Marks'] for student in collection.find({}) if student['Marks']==100.00]

print(students)