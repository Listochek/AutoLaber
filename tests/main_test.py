''' Тесты для проверки сколько изображений скачалось'''
import os


def check_images(number_of_pictures: int, save_dir: str, folder_name: str = 'Crawler') -> float:
   '''Test to count how many images were downloaded'''
   pic_cou = len(os.listdir(f'{save_dir}/{folder_name}'))
   return [pic_cou, pic_cou/number_of_pictures * 100]