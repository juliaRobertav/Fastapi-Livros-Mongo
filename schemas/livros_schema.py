
def livro_serializer(livro) -> dict:
    return {
        "id": str(livro["id"]),
        "nome": livro["nome"],
        "genero": livro["genero"],
        "autor": livro["autor"],
        "editora": livro["editora"],
    }
    
def livros_serializer(livros) -> list:
    return [livro_serializer(livro) for livro in livros],