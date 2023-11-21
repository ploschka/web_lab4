# импортируем необходимые модули
from jinja2 import Template
import sqlite3
import library_model as lm
# устанавливаем соединение с базой данных (базу данных взять из ЛР 1)
conn = sqlite3.connect("library.sqlite")
# выбираем записи из таблицы publisher

# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open('library_temp.jinja', 'r', encoding='utf-8')
html = f_template.read()
f_template.close()
# создаем объект-шаблон
template = Template(html)
# генерируем результат на основе шаблона
result_html = template.render(
    publisher="publisher",
    publisher_table=lm.get_publisher(conn),
    genre="genre",
    genre_table=lm.get_genre(conn),
    reader="reader",
    reader_table=lm.get_reader(conn),
    book="book",
    book_table=lm.get_book(conn),
    book_author="book_author",
    book_author_table=lm.get_book_author(conn),
    book_reader="book_reader",
    book_reader_table=lm.get_book_reader(conn),
    len=len
)
# создаем файл для HTML-страницы
f = open('library.html', 'w', encoding='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
conn.close()
