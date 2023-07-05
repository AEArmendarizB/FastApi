from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional


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
    id: Optional[int] 
    tittle:str = Field(min_length=3)
    author: str = Field(min_length=1)
    descripcion: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6) # range between 0-5

    class Config:
        schema_extra = {
            "example":{
                'tittle':'A new book',
                'author': 'Andres',
                'descripcion': 'A new desciption of a book',
                'rating':5
            }
        }


BOOKS = [
    Book(1,'Computer Science Pro', 'Andres','A very nice book',5),
    Book(2,'Be Fast with FastAPI', 'Andres','A great book',5),
    Book(3,'Master Endpoints', 'Andres','Awesame book',5),
    Book(4,'HP1', 'Author1','Book Decription',2),
    Book(5,'HP2', 'Author2','Book Decription',3),
    Book(6,'HP3', 'Author3','Book Decription',1)
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/")
async def read_book_by_rating(book_rating:int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))
    

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id+1
   
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id +1
    #     print(BOOKS[-1].id)
    # else:
    #     book.id = 1
    return book