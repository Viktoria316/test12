import logging
import os
import time

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("")
logging.info("")
logging.info("")

# os.walk
# os.path.join
# os.path.getmtime
# os.path.getsize
# os.path.dirname

os_walk = os.walk
logging.info(os_walk)

directory = '.'

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(root)
    # filetime = time.time()
    filetime = os.path.getmtime(root)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(root)
    parent_dir = os.path.dirname(root)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')