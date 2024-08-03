import sys
import os

# Добавляем корневую директорию в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ztest_folder.listcrawl import bing_list_crawler


from main_test import check_images, image_weight, process_images_in_directory, find_duplicate_images, get_image_sizes, repeating_size_counter


KEYS = ['котики', 'мышки', 'коты']
direct = 'picture'
kef = 5
#bing_list_crawler(KEYS, direct, kef)

def runing_test(key_words: list, main_dirr: str, max_pic: int = 2, folders_for_saving: list = ['train', 'validation', 'test']):
    path_to_images = [] # получаем через folders_for_saving


print(check_images(len(KEYS) * kef, direct)) #переписать функцию через лен массива тк все пути в одном списке path_to_images
print(image_weight(direct)) # переписать логику через уже готовые пути
print(process_images_in_directory(direct)) # проверка на то сломано ли изображение
print(find_duplicate_images(direct)) # можно не использовать тк уже реализовано в основной логике
#print(get_image_sizes(direct))
print(repeating_size_counter(get_image_sizes(direct))) #не знаю что это



