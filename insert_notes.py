import sqlite3
from datetime import date
db = sqlite3.connect('sqlite_python.db')
cursor=db.cursor()

# # Добавление данных
def add_new_notes():
    menu = int(input("Нажмите 1, если хотите добавить заметку в картотеку, нужно добавить: \n1. Добавить  заголовок заметки \n2. Содержание \n3. Дата \n"))
    if menu == 1:
        title = input('Заголовок заметки: ')
        body = input('Содержание: ')
   
    cursor.execute("SELECT COUNT(*) from notes WHERE title = '"+  title +"'")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        print('такая заметка есть в картотеке')                                 
    else:
        print(f'заметка {title} добавлена')                                              
        cursor.execute("INSERT INTO notes(title, body, joiningData) VALUES(?,?,?)", (title, body, date.today()))
        db.commit()
# add_new_notes()