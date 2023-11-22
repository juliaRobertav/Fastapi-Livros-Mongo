# main.py
from fastapi import FastAPI
from routes.livros_routes import livro_router

app = FastAPI()

app.include_router(livro_router, prefix="/livros", tags=["livros"])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)