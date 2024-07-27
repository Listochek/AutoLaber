''' Тесты для проверки сколько изображений скачалось'''
import os
from concurrent.futures import ThreadPoolExecutor
from statistics import median
from PIL import Image

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


