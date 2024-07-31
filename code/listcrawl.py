from icrawler.builtin import BingImageCrawler
import os
import shutil
import hashlib
from collections import defaultdict
import random


class FolderManager:
    def __init__(self) -> None:
        pass

    def add_folders(parent_dir: str, folders_names: list) -> list:
        path_list = []
        for i in folders_names:
            path = os.path.join(parent_dir, i)
            path_list.append(path)
            os.makedirs(path, exist_ok=True)
        return path_list

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
    '''add_folders -> *ranaming ->separation'''
    def __init__(self) -> None:
        pass

    def shuffle_imgs(self, images_dir: str) -> list: # random = True/False
        all_files = os.listdir(images_dir)
        random.shuffle(all_files)
        return all_files 

    def separation_files(self, all_files: list, folder_sizes: list):
        total_files = len(all_files)
        train_end = int(total_files * folder_sizes[0] / 100)
        validation_end = int(total_files * folder_sizes[2] / 100)

        train_files = all_files[:train_end]
        validation_files = all_files[train_end:validation_end]
        test_files = all_files[validation_end:]
        return [train_files, validation_files, test_files]
    '''    
    def move_files(files, target_dir):
        for file in files:
            shutil.move(os.path.join(images_dir, file), os.path.join(target_dir, file))'''

    def add_folders(self, images_dir: str, folder_names: list) -> list:
        for i in folder_names:
            if os.path.isdir(f'{images_dir}\\{i}'):
                shutil.rmtree(f'{images_dir}\\{i}')
        #FolderManager.remove_dirs(parent_dir, folder_names)
        return FolderManager.add_folders(images_dir, folder_names)

    def ranaming():
        pass

    def runer(self, parrent_dir:str, images_dir: str, folder_sizes: list = [75, 20, 5], folder_names: list = ['train', 'validation', 'test'], random_names:bool = False): #, random: bool = False, renaming_picture: bool = False
        self.add_folders(parrent_dir, folder_names)
        all_files = self.shuffle_imgs(images_dir)
        al = self.separation_files(all_files, folder_sizes)
        print(al)
     

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
            return duplicates
            
        else:
            self.drop_dublicate(duplicates)
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



duplicate_remover = RemoveDuplicate()
fold =  FolderSeparation()
fold.runer('picture', 'picture\\Crawler', folder_names=['train', 'validation', 'test'])
# Вызов метода find_duplicate_images через экземпляр класса
#duplicate_remover.find_duplicate_images(folder_path='picture\Crawler', delite_picture=False)