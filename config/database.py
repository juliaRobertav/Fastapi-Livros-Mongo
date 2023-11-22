from pymongo import MongoClient

cliente = MongoClient("mongodb+srv://julia:<ju123456>@fastapi.qmoukso.mongodb.net/julia?retryWrites=true&w=majority")

db = cliente.get_database('fastapi')

#todo_application

collection_livro = db["todos_app"]