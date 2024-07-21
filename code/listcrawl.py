from icrawler.builtin import BingImageCrawler
import os
import shutil


# можно было бы добавить номер откуда начинаются картинк

def bing_list_crawler(key_words: list, Save_path: str, max_pic: int = 1, synonym: bool = False, main_folder_name: str = 'Crawler'):
    add_folders(Save_path, key_words)
    os.makedirs(f'{Save_path}\\{main_folder_name}')
    for i in key_words:
    
        bing_crawler = BingImageCrawler(storage={'root_dir': f'{Save_path}/{i}'})
        bing_crawler.crawl(keyword=i, max_num=max_pic, file_idx_offset=0)
    piture_rename(Save_path, get_all_filenames(Save_path), main_folder_name)

def add_folders(parent_dir: str, folders_names: list):
    for i in folders_names:
        path = os.path.join(parent_dir, i) # ДОБАВИТЬ TRY EXECPT
        os.makedirs(path)
    
    print(folders_names)

def piture_rename(parent_dir: str, folders_names: list, main_folder_name: str):
    #os.path.join(parent_dir, main_folder_name) # ДОБАВИТЬ TRY EXECPT
    #os.makedirs(main_folder_name)
    for i in folders_names:
        if i == main_folder_name:
            continue
        else:
            for j in range(len(i)):
                print(i, j)
   # shutil.move()

def get_all_filenames(dirr: str) -> list:
    dir_list = os.listdir(dirr)
    return dir_list




keys = ['котики', 'мышки', 'коты']
bing_list_crawler(keys, 'TESTS', 3)