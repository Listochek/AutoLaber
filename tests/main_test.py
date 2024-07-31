''' Тесты для проверки сколько изображений скачалось'''
import os
from concurrent.futures import ThreadPoolExecutor
from statistics import median
from PIL import Image
import hashlib
from collections import defaultdict
import shutil

def check_images(number_of_pictures: int, parrent_dir: str, folder_name: str = 'Crawler') -> list:
   '''Test to count how many images were downloaded'''
   pic_cou = len(os.listdir(f'{parrent_dir}/{folder_name}'))
   return [pic_cou, pic_cou/number_of_pictures * 100]

def image_weight(parrent_dir: str, folder_name: str = 'Crawler') -> list: 
   parse_list = os.listdir((f'{parrent_dir}/{folder_name}'))
   image_weight_list = []
   for i in parse_list:
      image_weight_list.append(round(os.path.getsize(f'{parrent_dir}/{folder_name}/{i}') / 1024, 1))
   return [max(image_weight_list), min(image_weight_list), median(image_weight_list)]

def check_image_openable(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return file_path, True
    except (IOError, SyntaxError) as e:
        return file_path, False

def process_images_in_directory(parrent_dir: str, folder_name: str = 'Crawler') -> True:
   '''If function returns a list, in the folder has broken file'''
   folder_path = f'{parrent_dir}/{folder_name}'
   image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
   with ThreadPoolExecutor(max_workers=10) as executor:  # Установите количество потоков по желанию
      results = executor.map(check_image_openable, image_files)
   Fail_list = []
   for file_path, result in results:
      if result:
         continue
      else:
         Fail_list.append(file_path)
   return Fail_list if len(Fail_list) != 0 else True



def find_duplicate_images(folder_path: str, delite_picture : bool = False):
   # Словарь для хранения хешей изображений
   hash_dict = defaultdict(list)
   # Перебираем файлы в папке
   for root, dirs, files in os.walk(folder_path):
      for file in files:
            # Проверяем, является ли файл изображением (можно добавлять другие форматы)
         if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
               file_path = os.path.join(root, file)
                # Создаем хеш изображения
               image_hash = hash_image(file_path)
               hash_dict[image_hash].append(file_path)

    # Возвращаем только повторяющиеся изображения
   duplicates = {hash_value: paths for hash_value, paths in hash_dict.items() if len(paths) > 1}
   # условие на удаление по повторению delite_picture = True
   if delite_picture==False:
      return duplicates
   else:
      drop_dublicate(duplicates)
      return duplicates

def hash_image(file_path) -> str:
    """Создает хеш файла изображения."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def drop_dublicate(duplicates: dict):
   keys_to_del = duplicates.keys()
   for i in keys_to_del:
      massik = duplicates.get(i, None)
      massik.pop(0)
      for j in massik:
         os.remove(j)
      

def get_image_sizes(folder_path) -> dict:
    sizes = {}
    # Перебираем файлы в указанной папке
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                # Открываем изображение и получаем его размеры
                with Image.open(file_path) as img:
                    sizes[file_path] = img.size  # (ширина, высота)

    return sizes

def repeating_size_counter(xui: dict):
   value_count = {}
   for value in xui.values():
      if value in value_count:
         value_count[value] += 1
      else:
         value_count[value] = 1
   print(value_count)
   return value_count
