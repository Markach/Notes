### я отдельно поработала с приложением, используя формат JSON. Мне легче дается возможность использовать формат сохранения данных sqlite, поэтому я и работала с ним в приложении 

import json

def createJson():  
    mydict = [ 
        {
            'id': 1,
            'title': 'Lesson',
            'body': 'first lecture on testing',
            'date': '2023-02-10'
        },
        {
            'id': 2,
            'title': 'Postcard',
            'body': 'send on wednesday',
            'date': '2023-02-15'
        },
        {
            'id': 3,
            'title': 'Dinner',
            'body': 'gala dinner on Friday',
            'date': '2023-02-15'
        }
    ]
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:  # октрытие файла и его значение присваеиваем переменнной
            json.dump(mydict, fs, indent=2)  # дополняем перемеенную, нашим словарем   можно сортировать sort_key=True
    except IOError as e:  # в случае возникновения ошибки
        print(e)  # выводит сообщение об ошибке
    print('Сохранение данных завершено!')
createJson()



# читаем файл
def loadData():
    try:
        with open('data.json') as f:
            data = json.load(f)
            return data
    finally:
        f.close()

# сохраняем в файл
def writeFile(newData):
    try:
        with open('data.json', 'w') as f:
            json.dump(newData, f, indent=2)
    finally:
        f.close()  

# добавляем новые данные
def addData(data):
    loadedData = loadData()
    dublicateCount = 0
    for d in loadedData:
        if data['title'] in d['title']:
            print(d['title'])
            dublicateCount += 1
    if dublicateCount == 0:
        loadedData.append(data)
        writeFile(loadedData)
        print('\n\nnote added!')
    else:
        print('title already exists!')  

def addNote():
    print('\nAdd Note\n')
    id = input('id: ')
    title = input('Title: ')
    body = input('body: ')
    date = input('date: ')
    data = {'id':id, 'title': title, 'body': body, 'date': date}
    addData(data)  
# addNote()  
                      

# выводим заметки
def listNotes():
    loadedData = loadData()
    print('\nID\tTitle\n')
    for data in loadedData:
        print(str(loadedData.index(data)+1) + '\t' + data['title'])
    print()

# удаление заметки
def removeNote(taskID):
    loadedData = loadData()
    itemIndex = None
    for data in loadedData:
        if taskID == loadedData.index(data)+1:
            itemIndex = loadedData.index(data)
    if(itemIndex != None):
        loadedData.pop(itemIndex)
        writeFile(loadedData)
        print('note removed!')
    else:
        print('no such note!')
# removeNote(5)        
listNotes()

# смотрим заметку
def viewNoteByID(noteID):
    loadedData = loadData()
    rNote = None
    for note in loadedData:
        if noteID == loadedData.index(note)+1:
            rNote = note
    if(rNote != None):
        print(str(rNote['id']) +' Title: ' + rNote['title'] + '\n\n' + rNote['body'] + '\n\n'+ rNote['date'] + '\n\n')
    else:
        print('note not found!')       
# viewNoteByID(4) 
      

#получаем все значения
f = open('data.json', encoding='utf-8')
d = f.read()
data = json.loads(d)  # это list нужно пройти по каждому элементу
for item in data:
    for key,value in item.items():
        print(key, ':', value)
    print()  
for vac in data:  # вывести только заголовки
    print(vac['title'])
for vac in data:
        print(vac['date'])  
print()      
