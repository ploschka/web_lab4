import sqlite3 as sql
import model as md
from jinja2 import Template

con = sql.connect("store.sqlite")
df = md.get_books_single_word_lower_or_higher(con, 500, 700)
con.close()

h = [i for i in df]
data = zip(*[[x for x in df[i]] for i in h])

out = open('index.html', 'w', encoding='utf-8')

with open('template.jinja', 'r', encoding='utf-8') as f:
    temp = Template(f.read())

result = temp.render(header=h, data=data)

out.write(result)
out.close()
