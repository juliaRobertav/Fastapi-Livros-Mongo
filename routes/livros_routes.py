from fastapi import APIRouter
from config.database import collection_livro
from models.livros_model import Livro
from schemas.livros_schema import livros_serializer
from bson import ObjectId

livro_router = APIRouter()


@livro_router.get("/")
async def get_livros():
    livros = livros_serializer(collection_livro.find())
    return {"status": "ok", "data": livros}

@livro_router.get("/{id}")
async def get_livro(id: str):
    livro = livros_serializer(collection_livro.find_one({"_id": ObjectId(id)}))
    return {"status": "ok", "data": livro}

@livro_router.post("/")
async def post_livro(livro: Livro):
    _id = collection_livro.insert_one(dict(livro))
    livro = livros_serializer(collection_livro.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": livro}

@livro_router.put("/{id}")
async def update_livro(id: str, livro:Livro):
    collection_livro.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(livro)
    })
    livro = livros_serializer(collection_livro.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": livro}

@livro_router.delete("/{id}")
async def delete_livro(id: str):
    collection_livro.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}