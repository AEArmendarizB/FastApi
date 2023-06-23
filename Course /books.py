from fastapi import FastAPI, Body


app = FastAPI()


BOOKS = [
    {'tittle':'Tittle One','author':'Author One','category':'science'},
    {'tittle':'Tittle Two','author':'Author Two','category':'science'},
    {'tittle':'Tittle Three','author':'Author Three','category':'history'},
    {'tittle':'Tittle Four','author':'Author Four','category':'language'},
    {'tittle':'Tittle Five','author':'Author Five','category':'math'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_tittle}")
async def read_book(book_tittle: str):
    for book in BOOKS:
        if book.get('tittle').casefold()==book_tittle.casefold():
            return book

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS: 
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
        return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author:str, category:str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
                book_to_return.append(book)
    return book_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(update_book =Body()):
    for i in range (len(BOOKS)):
        if BOOKS[i].get('tittle').casefold() == update_book.get('tittle').casefold():
            BOOKS[i] = update_book