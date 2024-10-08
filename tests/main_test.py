''' Различные тесты над скаченными изображениями'''
import os
from concurrent.futures import ThreadPoolExecutor
from statistics import median
from PIL import Image
import hashlib
from collections import defaultdict

def check_images(pic_list: list, key_words: list, max_pic: int) -> list:
   '''Test to count how many images were downloaded'''
   pic_cou = len(key_words) * max_pic
   return [len(pic_list), f'{len(pic_list)/pic_cou * 100}%']

def image_weight(pic_list: list) -> dict: 
   image_weight_list = []
   for i in pic_list:
      image_weight_list.append(round(os.path.getsize(i) / 1024, 1))
   return {'max, KB': max(image_weight_list), 'min, KB': min(image_weight_list), 'median, KB': median(image_weight_list)}

def check_image_openable(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return file_path, True
    except (IOError, SyntaxError) as e:
        return file_path, False

def broken_pictures(image_files: list) -> False:
   '''If function returns a list, in the folder has broken file'''
   with ThreadPoolExecutor(max_workers=10) as executor: 
      results = executor.map(check_image_openable, image_files)
   Fail_list = []
   for file_path, result in results:
      if result:
         continue
      else:
         Fail_list.append(file_path)
   return Fail_list if len(Fail_list) != 0 else False



def find_duplicate_images(folder_path: str, delite_picture : bool = False):
   hash_dict = defaultdict(list)
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
