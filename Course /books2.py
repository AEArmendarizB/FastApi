from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()

class Book:
    id: int
    tittle:str
    author: str
    descripcion: str
    rating: int
    publish_date: int

    def __init__(self,id,tittle,author,descripcion,rating,publish_date):
        self.id = id
        self.tittle = tittle
        self.autho = author
        self.descripcion = descripcion
        self.rating = rating
        self.publish_date = publish_date

class BookRequest(BaseModel):
    id: Optional[int] 
    tittle:str = Field(min_length=3)
    author: str = Field(min_length=1)
    descripcion: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6) # range between 0-5
    publish_date: int = Field(gt=1999, lt=2031) #range between 2000-2031

    class Config:
        schema_extra = {
            "example":{
                'tittle':'A new book',
                'author': 'Andres',
                'descripcion': 'A new desciption of a book',
                'rating':5,
                'publish_date':2023
            }
        }


BOOKS = [
    Book(1,'Computer Science Pro', 'Andres','A very nice book',5,2030),
    Book(2,'Be Fast with FastAPI', 'Andres','A great book',5,2020),
    Book(3,'Master Endpoints', 'Andres','Awesame book',5,2028),
    Book(4,'HP1', 'Author1','Book Decription',2,2030),
    Book(5,'HP2', 'Author2','Book Decription',3,2027),
    Book(6,'HP3', 'Author3','Book Decription',1,2026)
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/")
async def read_book_by_rating(book_rating:int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))
    

@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed =  True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/publish_date/")
async def read_books_by_publish_date(publish_date: int = Query(gt=1999, lt=2031)):
    book_to_return = []
    for book in BOOKS: 
        if book.publish_date == publish_date:
            book_to_return.append(book)
    return book_to_return



def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id+1
   
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id +1
    #     print(BOOKS[-1].id)
    # else:
    #     book.id = 1
    return book