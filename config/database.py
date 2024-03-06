from pymongo import MongoClient

cliente = MongoClient("mongodb+srv://username:<password>@fastapi.qmoukso.mongodb.net/julia?retryWrites=true&w=majority")

db = cliente.get_database('fastapi')

#todo_application

collection_livro = db["todos_app"]
