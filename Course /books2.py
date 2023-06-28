from fastapi import FastAPI,Body
from pydantic import BaseModel


app = FastAPI()

class Book:
    id: int
    tittle:str
    author: str
    descripcion: str
    rating: int

    def __init__(self,id,tittle,author,descripcion,rating):
        self.id = id
        self.tittle = tittle
        self.autho = author
        self.descripcion = descripcion
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    tittle:str
    author: str
    descripcion: str
    rating: int


BOOKS = [
    Book(1,'Computer Science Pro', 'Andres','A very nice book',5),
    Book(2,'Be Fast with FastAPI', 'Andres','A great book',5),
    Book(3,'Master Endpoints', 'Andres','Awesame book',5),
    Book(4,'HP1', 'Author1','Book Decription',2),
    Book(5,'HP2', 'Author2','Book Decription',3),
    Book(5,'HP3', 'Author3','Book Decription',1)
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = BOOKS(**book_request.dict())
    BOOKS.append(new_book)
    
