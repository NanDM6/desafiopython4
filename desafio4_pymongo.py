import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient(
    "mongodb+srv://renangoncal:YAuhaAJx7rLXVZpq@cluster0.20idnjo.mongodb.net/?retryWrites=true&w=majority"
)

db = client.test
collection = db.test_collection
print(db.test_collection)

# definição de infor para compor o doc
post = {
    "name": "juliana",
    "cpf": "1234567890",
    "endereco": "rua macarone",
    "tipo_conta": "corrente",
    "agencia": "1001",
    "num_conta": "5529302",
    "saldo": "1000.23",
    "date": datetime.datetime.utcnow(),
}

# preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# print(db.posts.find_one())
pprint.pprint(db.posts.find_one())

# bulk inserts
new_posts = [
    {
        "name": "sandy",
        "cpf": "2345678901",
        "endereco": "travessa cambui",
        "tipo_conta": "poupanca",
        "agencia": "1001",
        "num_conta": "7729302",
        "saldo": "100",
        "date": datetime.datetime.utcnow(),
    },
    {
        "name": "patrick",
        "cpf": "3456789012",
        "endereco": "rua luis silva",
        "tipo_conta": "corrente",
        "agencia": "1001",
        "num_conta": "6629302",
        "saldo": "-200",
        "date": datetime.datetime.utcnow(),
    },
]

result = posts.insert_many(new_posts)
print(result.inserted_ids)

print("\nRecuperação final")
pprint.pprint(db.posts.find_one({"name": "juliana"}))

print("\n Documentos presentes na coleção posts")
for post in posts.find():
    pprint.pprint(post)
