import delete_notes as de
import insert_notes as ins
import select_notes as s
import update_notes as up


def choose():
    print('''\n1. Посмотреть все заметки; \n2. Выбрать по заголовку заметки; \n3. Выбрать по точной дате(формат гггг-мм-дд);\n4. Выбрать за текущий день(day), за неделю(week), за месяц(month); \n5. Удалить данные по заголовку заметки; \n6. Добавление заметки; \n7. Обновление заметки; \n8. Выход''')
    while True:
        
        choice = input('\nВыберите вариант и введите цифру: ')
        if choice == '1':
            s.select_all()
        if choice == '2':
            s.select_title()
        if choice == '3':
            s.select_time()
        if choice == '4':
            s.select_time2()
        if choice == '5':
            de.del_notes() 
        if choice == '6':
            ins. add_new_notes()
        if choice == '7':
            up. update_multiple_columns()      
        if choice == '8':
            print('\nДо скорой встречи!\n')
            break