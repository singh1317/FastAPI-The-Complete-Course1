from fastapi import Body, FastAPI

app = FastAPI()



BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books") #http://127.0.0.1:8000/books
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}") #http://127.0.0.1:8000/books/Title%20One
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        

@app.get("/books/") #http://127.0.0.1:8000/books/?category=math
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# Get all books from a specific author using path or query parameters
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{book_author}/") #http://127.0.0.1:8000/books/Author%20Two/?category=math
async def read_category_by_query2(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book") # => {"title": "Title Six6", "author": "Author Two", "category": "math"}
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book") # => {"title": "Title Six6", "author": "Author 2", "category": "math"}
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}") # Title Six6
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break





##uvicorn books1:app --reload
## fastapi run books1.py
## fastapi dev books1.py
## http://127.0.0.1:8000
## http://127.0.0.1:8000/docs#/