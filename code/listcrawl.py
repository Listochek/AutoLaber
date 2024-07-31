from icrawler.builtin import BingImageCrawler
import os
import shutil
import hashlib
from collections import defaultdict

class FolderManager:
    def __init__(self) -> None:
        pass

    def add_folders(parent_dir: str, folders_names: list) -> None:
        for i in folders_names:
            path = os.path.join(parent_dir, i)
            os.makedirs(path)

    def piture_rename(parent_dir: str, main_folder_name: str, folders_names: list) -> None: 
        folders_names.remove(main_folder_name)
        print(folders_names)
        for i in folders_names:
            pathik = f'{parent_dir}/{i}' 
            print(os.listdir(pathik))
            list_iteration = os.listdir(pathik)
            for j in list_iteration:
                shutil.move(f'{parent_dir}/{i}/{j}', f'{parent_dir}/{main_folder_name}/{i + j}')
        FolderManager.remove_dirs(parent_dir, folders_names)

    def get_all_filenames(dirr: str) -> list:
        dir_list = os.listdir(dirr)
        return dir_list

    def remove_dirs(parent_dir: str, folders_names: list) -> None:
        for i in folders_names:
            shutil.rmtree(f'{parent_dir}/{i}')

    def remove_old_folder(parent_dir: str) -> None:
        if os.path.isdir(parent_dir):
            shutil.rmtree(parent_dir)

# в траейн 75% вал 20% в тест 5%
class FolderSeparation:
    def __init__(self) -> None:
        self.runer()

    def drop_duplicates():
        pass
    def separation(): # random = True/False
        pass  
    def add_folders(): 
        pass
    def ranaming():
        pass

    def runer(folder_sizes: list = [75, 20, 5], random: bool = False, renaming_picture: bool = False):
        """
            folder_sizes = [75, 20, 5] 

            75% - pictures on train, 
            20% - pictures on vallidation, 
            5% - pictures on test
        
            random = False

            True - random distribution of pictures
            False - sequential image division
        """
        pass

class RemoveDuplicate():
    
    def __init__(self) -> None:
        pass
    
    def find_duplicate_images(self, folder_path: str, delite_picture : bool = False):
        # Словарь для хранения хешей изображений
        hash_dict = defaultdict(list)
        # Перебираем файлы в папке
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                    # Проверяем, является ли файл изображением (можно добавлять другие форматы)
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    file_path = os.path.join(root, file)
                        # Создаем хеш изображения
                    image_hash = self.hash_image(file_path)
                    hash_dict[image_hash].append(file_path)

            # Возвращаем только повторяющиеся изображения
        duplicates = {hash_value: paths for hash_value, paths in hash_dict.items() if len(paths) > 1}
        # условие на удаление по повторению delite_picture = True
        if delite_picture==False:
            print(duplicates)
            return duplicates
            
        else:
            self.drop_dublicate(duplicates)
            print(f'{duplicates} - БЫЛИ ДРОПНУТЫ')
            return duplicates

    def hash_image(self, file_path) -> str:
        """Создает хеш файла изображения."""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def drop_dublicate(self, duplicates: dict):
        keys_to_del = duplicates.keys()
        for i in keys_to_del:
            massik = duplicates.get(i, None)
            massik.pop(0)
            for j in massik:
                os.remove(j)   

'''    def process_duplicates(self, ):
        pass'''
    

'''
def bing_list_crawler(key_words: list, Save_path: str, max_pic: int = 1, main_folder_name: str = 'Crawler', synonym: bool = False):
    FolderManager.remove_old_folder(Save_path)
    FolderManager.add_folders(Save_path, key_words)
    os.makedirs(f'{Save_path}\\{main_folder_name}')
    for i in key_words:
        bing_crawler = BingImageCrawler(storage={'root_dir': f'{Save_path}/{i}'})
        bing_crawler.crawl(keyword=i, max_num=max_pic, file_idx_offset=0)
    FolderManager.piture_rename(Save_path, main_folder_name, FolderManager.get_all_filenames(Save_path))
#FolderSeparation.runer()'''

duplicate_remover = RemoveDuplicate()

# Вызов метода find_duplicate_images через экземпляр класса
duplicate_remover.find_duplicate_images(folder_path='picture\Crawler', delite_picture=True)