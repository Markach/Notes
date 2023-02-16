import sqlite3

db = sqlite3.connect('sqlite_python.db')
cursor=db.cursor()

# Выборка данных
#  по дате
def select_time():
    variable = input('Введите дату, из которой хотите выбирать ')
    cursor.execute("SELECT * from notes   WHERE joiningData = '"+  variable +"'")
    result = cursor.fetchall()
    if result == None:
        print('Нет заметок в такую дату в картотеке!') 
    else:
        cursor.execute("SELECT * from notes   WHERE joiningData = '"+  variable +"'")
        db.commit()
        print(result)
# select_time()

# название заголовка заметки
def select_title():
    variable = str.capitalize(input('Введите заголовок заметки '))
    cursor.execute("SELECT * from notes   WHERE title = '"+  variable +"'")
    result = cursor.fetchall()

    if result == None:
        print('Нет заметки с таким заголовком в картотеке!')   
    else:
        cursor.execute("SELECT * from notes   WHERE title= '"+ variable +"'")
        db.commit()
    print(result)
# select_title()

# все
def select_all():
    cursor.execute("SELECT * from notes ")
    result = cursor.fetchall()
    print(result)
# select_all()  


def select_time2(within = "all"):
    input('Введите время, за которое хотите просмотреть заметки(за day, week, month) ')
    if(within == "day"):
        result = cursor.execute("SELECT * FROM notes WHERE joiningData BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime') ORDER BY `joiningData`")  
        print(result.fetchall())
    elif(within == "week"):
        result = cursor.execute("SELECT * FROM notes WHERE joiningData BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ORDER BY `joiningData`")  
        print(result.fetchall())    
    elif(within == "month"):
        result = cursor.execute("SELECT * FROM notes WHERE joiningData BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') ORDER BY `joiningData`")  
        print(result.fetchall()) 
    else:
        result = cursor.execute("SELECT * FROM notes WHERE joiningData")  
        print(result.fetchall())    

select_time2(input('Введите время, за которое хотите просмотреть заметки(за day, week, month) '))        
# select_time2()