from pandas import read_sql

def get_publisher(conn):
    return read_sql("SELECT * FROM publisher", conn)

def get_genre(conn):
    return read_sql("SELECT * FROM genre", conn)

def get_reader(conn):
    return read_sql("SELECT * FROM reader", conn)

def get_book(conn):
    return read_sql("SELECT * FROM book", conn)

def get_book_author(conn):
    return read_sql("SELECT * FROM book_author", conn)

def get_book_reader(conn):
    return read_sql("SELECT * FROM book_reader", conn)
