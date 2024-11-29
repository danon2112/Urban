import time
import os

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(file)
        filetime = time.ctime(os.path.getmtime(file))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {filetime}, Родительская директория: {parent_dir}')