import sqlite3
from datetime import date

def update_multiple_columns():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        variable = str.capitalize(input('Введите заголовок заметки, которую нужно изменить: '))
        cursor.execute("SELECT COUNT(*) from notes WHERE title = '"+  variable +"'")
        result = cursor.fetchone()

        if int(result[0]) == 0:
            print(f'заметки с таким заголовком:  {variable} нет в картотеке! ')
        else:
            new = input('Введите новое содержание заметки: ')
            dat = date.today()
            sqlite_update_query = """Update notes set body = ?, joiningData = ? where title = ?"""
            column_values = (new, dat, variable)
            cursor.execute(sqlite_update_query, column_values)
            sqlite_connection.commit()
            print("Заметка и дата ее создания успешно обновлены")
            sqlite_connection.commit()
            cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()        

# update_multiple_columns()  