import pprint

import pymongo as pyM

client = pyM.MongoClient(
    "mongodb+srv://renangoncal:YAuhaAJx7rLXVZpq@cluster0.20idnjo.mongodb.net/?retryWrites=true&w=majority"
)
db = client.test
posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print("\nContagem total e contagem filtrada:")
print(posts.count_documents({}))
print(posts.count_documents({"name": "juliana"}))

print("\nFiltragem por saldo:")
pprint.pprint(posts.find_one({"saldo": "100"}))

print("\nRecuperando info da coleção post de maneira ordenada")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)


"""
print("\nCriando indice sem duplicacoes:")
result = db.profiles.create_index([("name", pyM.ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))


user_profile_user = [{"user_id": 211, "name": "Luke"}, {"user_id": 212, "name": "Joao"}]

result = db.profile_user.insert_many(user_profile_user)

print("\nColeções armazenadas no mongoDB")
collections = db.list_collection_names()

print("\nManeiras de deletar:")
# db['profiles'].drop()

for collection in collections:
    print(collection)

for post in posts.find():
    pprint.pprint(post)

# print(posts.delete_one({"author": "Mike"}))
# print(posts.delete_many({"author": "Mike"}))
# print(db.profile_user.drop())

client.drop_database("test")

print(db.list_collection_names())
"""
