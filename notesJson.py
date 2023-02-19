### я отдельно поработала с приложением, используя формат JSON. Мне легче дается возможность использовать формат сохранения данных sqlite, поэтому я и работала с ним в приложении 

import argparse
import json
import datetime
import os


def load_notes(file_path):
    """Загрузка заметок из файла"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []


def save_notes(notes, file_path):
    """Сохранение заметок в файл"""
    with open(file_path, 'w') as file:
        json.dump(notes, file, indent=4)


def add_note(notes, title, body):
    """Добавление заметки"""
    new_note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'created_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(new_note)
    return new_note


def edit_note(notes, note_id, title=None, body=None):
    """Редактирование заметки"""
    note = get_note_by_id(notes, note_id)
    if note:
        note['title'] = title if title else note['title']
        note['body'] = body if body else note['body']
        note['updated_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return note


def delete_note(notes, note_id):
    """Удаление заметки"""
    note = get_note_by_id(notes, note_id)
    if note:
        notes.remove(note)
        return note


def get_note_by_id(notes, note_id):
    """Получение заметки по идентификатору"""
    for note in notes:
        if note['id'] == note_id:
            return note


def list_notes(notes):
    """Вывод списка заметок"""
    for note in notes:
        print(f"{note['id']} {note['title']} ({note['created_at']})")


def main():
    parser = argparse.ArgumentParser(description='Консольное приложение заметки')
    parser.add_argument('file_path', type=str, help='Путь к файлу с заметками')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Добавление новой заметки')
    add_parser.add_argument('title', type=str, help='Заголовок заметки')
    add_parser.add_argument('body', type=str, help='Тело заметки')

    edit_parser = subparsers.add_parser('edit', help='Редактирование существующей заметки')
    edit_parser.add_argument('id', type=int, help='Идентификатор заметки')
    edit_parser.add_argument('--title', type=str, help='Новый заголовок заметки')
    edit_parser.add_argument('--body', type=str, help='Новое тело заметки')     
