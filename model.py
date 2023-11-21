from sqlite3 import Connection
from pandas import read_sql

def get_books_single_word_lower_or_higher(con:Connection, price1:int, price2:int):
    return read_sql('''                 
        SELECT title as 'Название', name_genre as 'Жанр', amount as 'Количество', price as 'Цена'
        FROM book
        INNER JOIN genre ON book.genre_id = genre.genre_id
        WHERE book.title NOT LIKE '% %'
        AND (price < :p_1 OR price > :p_2)
        ORDER BY 'Название' ASC, 'Жанр' ASC
        ''', con, params={"p_1": price1, "p_2": price2})
