from fastapi import FastAPI


app = FastAPI()


BOOKS = [
    {'tittle':'Tittle One','author':'Author One','category':'science'},
    {'tittle':'Tittle Two','author':'Author Two','category':'math'},
    {'tittle':'Tittle Three','author':'Author Three','category':'history'},
    {'tittle':'Tittle Four','author':'Author Four','category':'language'},
    {'tittle':'Tittle Five','author':'Author Five','category':'math'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS