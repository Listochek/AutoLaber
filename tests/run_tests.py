import sys
import os
#from test_set_log import testus
# Добавляем корневую директорию в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from ztest_folder.listcrawl import bing_list_crawler
from tests.test_set_log import add_logs

from tests.main_test import check_images, image_weight, broken_pictures, find_duplicate_images, get_image_sizes, repeating_size_counter
from file_management.folder_manager import FolderManager

KEYS = ['котики', 'мышки', 'коты']
direct = 'picture'
kef = 5
#bing_list_crawler(KEYS, direct, kef)


def runing_test(key_words: list, main_dirr: str, max_pic: int = 2, folders_for_saving: list = ['train', 'validation', 'test']):
    # -- logs -- #
    from tests.test_set_log import add_logs
    logger = add_logs()

    # 1. Определяем новый уровень логирования

    # -- logs -- #
    suk = FolderManager()# ренеймнуть
    path_to_images = suk.get_filenames_in_dirrectores(dirr=main_dirr, folders=folders_for_saving) # получаем через folders_for_saving
    logger.test(f'check_images: {check_images(pic_list=path_to_images, key_words=key_words, max_pic=max_pic)}')
    logger.test(f'image_weight: {image_weight(path_to_images)}')
    logger.test(f'broken images: {broken_pictures(path_to_images)}')

#runing_test(KEYS, 'picture', 15)
#print(check_images(len(KEYS) * kef, direct)) #переписать функцию через лен массива тк все пути в одном списке path_to_images
#print(image_weight(direct)) # переписать логику через уже готовые пути
#print(v) # проверка на то сломано ли изображение
#print(find_duplicate_images(direct)) # можно не использовать тк уже реализовано в основной логике
#print(get_image_sizes(direct)) # пересмотреть тк не нужно узновать все изоюражения, интересно посмотреть отклонения
#print(repeating_size_counter(get_image_sizes(direct))) #не знаю что это



