'''Функция для рана всего проекта которая принимает достаточно много параметров'''
#from icrawler import BingImageCrawler
import sys
import os
from icrawler.builtin import BingImageCrawler

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_management.folder_manager import FolderManager, FolderSeparation


def run_ansambl(key_words: list, path_to_save: str, max_pic: int = 1, folders_for_saving: list = ['train', 'validation', 'test'], crawler: str = 'Crawler'):
    folmg, folsep = FolderManager(), FolderSeparation()
   # folders_for_saving.append(crawler)
    folmg.remove_dirs(path_to_save, folders_for_saving)
    #folmg.remove_old_folder(path_to_save)
    

KEYS = ['котики', 'мышки', 'коты']
run_ansambl(KEYS, 'picture')


#bing_list_crawler(KEYS, 'TESTS', 65)

'''def bing_list_crawler(key_words: list, Save_path: str, max_pic: int = 1, main_folder_name: str = 'Crawler', synonym: bool = False):
    FolderManager.remove_old_folder(Save_path) # перезаписать для разделения через объект с наследованием
    FolderManager.add_folders(Save_path, key_words)
    os.makedirs(f'{Save_path}\\{main_folder_name}')
    for i in key_words:
        bing_crawler = BingImageCrawler(storage={'root_dir': f'{Save_path}/{i}'})
        bing_crawler.crawl(keyword=i, max_num=max_pic, file_idx_offset=0)
    FolderManager.piture_rename(Save_path, main_folder_name, FolderManager.get_all_filenames(Save_path))'''