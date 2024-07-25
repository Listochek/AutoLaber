from icrawler.builtin import BingImageCrawler
import os
import shutil


# можно было бы добавить номер откуда начинаются картинк
class BingImageCrawlerList:
    def __init__(self) -> None:
        pass

    def add_folders( parent_dir: str, folders_names: list):
        for i in folders_names:
            path = os.path.join(parent_dir, i)
            os.makedirs(path)

    def piture_rename(parent_dir: str, main_folder_name: str, folders_names: list): 
        folders_names.remove(main_folder_name)
        print(folders_names)
        for i in folders_names:
            pathik = f'{parent_dir}/{i}' #{main_folder_name}/
            print(os.listdir(pathik))
            list_iteration = os.listdir(pathik)
            for j in list_iteration:
                #print(f'{parent_dir}/{i}/{j}')
                #print(f'{parent_dir}/{main_folder_name}/{i + j}')
                shutil.move(f'{parent_dir}/{i}/{j}', f'{parent_dir}/{main_folder_name}/{i + j}')
        BingImageCrawlerList.remove_dirs(parent_dir, folders_names)

    def get_all_filenames(dirr: str) -> list:
        dir_list = os.listdir(dirr)
        return dir_list

    def remove_dirs(parent_dir: str, folders_names: list):
        for i in folders_names:
            shutil.rmtree(f'{parent_dir}/{i}')

def bing_list_crawler(key_words: list, Save_path: str, max_pic: int = 1, synonym: bool = False, main_folder_name: str = 'Crawler'):
    
    if os.path.isdir(Save_path):
        shutil.rmtree(Save_path)

    BingImageCrawlerList.add_folders(Save_path, key_words)
    os.makedirs(f'{Save_path}\\{main_folder_name}')
    for i in key_words:
        bing_crawler = BingImageCrawler(storage={'root_dir': f'{Save_path}/{i}'})
        bing_crawler.crawl(keyword=i, max_num=max_pic, file_idx_offset=0)
    print(BingImageCrawlerList.get_all_filenames(Save_path))
    BingImageCrawlerList.piture_rename(Save_path, main_folder_name, BingImageCrawlerList.get_all_filenames(Save_path))

KEYS = ['котики', 'мышки', 'коты']
bing_list_crawler(KEYS, 'TESTS', 3)