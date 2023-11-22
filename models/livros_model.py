from pydantic import BaseModel

class Livro(BaseModel):
    nome: str
    genero: str
    autor: str
    editora: str