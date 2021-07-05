from pprint import pprint

from yadisk import YandexDisk
from stackof import stack_q, get_dates
from superhero import find_hero_id


if __name__ == '__main__':
    find_hero_id() #Определяем кто самый умный супергерой


    # ya = YandexDisk(r'E:\Temp\Local_file_on_disk.txt')  #Запись с диска
    # ya = YandexDisk('files/file_to_upload.txt')         #Запись из папки проекта
    # ya = YandexDisk('test_in_main.txt')                 #Запись из корня проекта
    # ya.mk_dir()                                         #Запись файлов на диск


    # pprint(stack_q())     #Вывод вопросов с stackoverflow за последние 2 дня