from pandas import read_sql


def get_reader(conn):
    return read_sql("SELECT * FROM reader", conn)


def get_book_reader(conn, id):
    return read_sql("""
                    SELECT title 'Название', author_name 'Авторы', borrow_date 'Дата выдачи', return_date 'Дата возврата'
                    FROM book_reader
                    NATURAL JOIN book
                    NATURAL JOIN book_author
                    NATURAL JOIN author
                    WHERE reader_id = :p_id
                    """, conn, params={"p_id": id})
