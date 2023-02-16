import sqlite3

db = sqlite3.connect('sqlite_python.db')
cursor=db.cursor()

# # Удаление данных по названию заголовка заметки
def del_notes():
    
    variable = str.capitalize(input('Введите заголовок заметки'))
    cursor.execute("SELECT COUNT(*) from notes WHERE title = '"+  variable+"'")
    result = cursor.fetchone()

    if int(result[0]) == 0:
        print(f'заметки с таким заголовком {variable} нет в картотеке! ')                        
    else:
        print(f'заметка {variable} удалена')                                                            
        cursor.execute("DELETE from notes WHERE title= '"+ variable+"'")
        db.commit()
# del_notes()