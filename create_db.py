import sqlite3, datetime
from datetime import date

def create_notes(title, body, joining_data):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS notes(
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        title text NOT NULL,
                                        body text NOT NULL,
                                        joiningData timestamp);'''


        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)

        # вставить заметку
        sqlite_insert_with_param = '''INSERT INTO 'notes'
                                ('title', 'body', 'joiningData')
                                VALUES(?,?,?);'''

        data_tuple = (title, body, joining_data)
        cursor.execute(sqlite_insert_with_param, data_tuple)  
        sqlite_connection.commit()
        print("Заметка успешно добавлена \n")  

        # получить данные в заметке
        sqlite_select_query = '''SELECT title, body, joiningData from notes WHERE id = ?'''
        cursor.execute(sqlite_select_query, (12,))
        records = cursor.fetchall()

        for row in records:
            title = row[0]
        cursor.close()  

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)   

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")                
            body = row[1] 
            joining_data = row[2]
            print("заметка", "'", title, "'", "добавлена", joining_data)
            print("содержание заметки: ", body)

#create_notes('Конспект', ' не забыть дописать по Python', date.today())   