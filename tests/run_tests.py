import sys
import os

# Добавляем корневую директорию в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from code.listcrawl import bing_list_crawler


from main_test import check_images, image_weight, process_images_in_directory, find_duplicate_images, get_image_sizes, repeating_size_counter


KEYS = ['котики', 'мышки', 'коты']
direct = 'picture'
kef = 5
#bing_list_crawler(KEYS, direct, kef)

print(check_images(len(KEYS) * kef, direct))
print(image_weight(direct))
print(process_images_in_directory(direct))
print(find_duplicate_images(direct))
#print(get_image_sizes(direct))
print(repeating_size_counter(get_image_sizes(direct)))



