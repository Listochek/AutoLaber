import os
import shutil
import random
import logging
from PIL import Image
class FolderManager:
    def __init__(self) -> None:
        pass

    def add_folders(self, parent_dir: str, folders_names: list) -> list:
        path_list = []
        for i in folders_names:
            path = os.path.join(parent_dir, i)
            path_list.append(path)
            os.makedirs(path) # , exist_ok=True
        logging.info(f'add folders: { {*path_list} }')
        return path_list


    def picture_rename(self, parent_dir: str, main_folder_name: str, folders_names: list) -> None: 
        folders_names.remove(main_folder_name)
        for i in folders_names:
            pathik = f'{parent_dir}/{i}' 
            list_iteration = os.listdir(pathik)
            for j in list_iteration:
                shutil.move(f'{parent_dir}/{i}/{j}', f'{parent_dir}/{main_folder_name}/{i + j}')
        self.remove_dirs(parent_dir, folders_names)


    def get_all_filenames(self, dirr: str) -> list:
        return os.listdir(dirr)
    # посмотреть на 
    def get_filenames_in_dirrectores(self, dirr: str, folders: list):
        paths = []
        for i in folders:
            the = os.listdir(f'{dirr}\\{i}')
            for j in the:
                paths.append(f'{dirr}\\{i}\\{j}')
        return paths
        
    
    def remove_dirs(self, parent_dir: str, folders_names: list) -> None:
        for i in folders_names:
            try:
                shutil.rmtree(f'{parent_dir}/{i}')
            except:
                logging.error(f"remove_dirs don't find {parent_dir}/{i}" )
                pass
    def remove_old_folder(self, parent_dir: str) -> None:
        if os.path.isdir(parent_dir):
            shutil.rmtree(parent_dir)


class FolderSeparation:
    #add_folders -> *ranaming ->separatio
    def __init__(self) -> None:
        pass

    def shuffle_imgs(self, images_dir: str) -> list: # random = True/False
        all_files = os.listdir(images_dir)
        for i in all_files:
            all_files[all_files.index(i)] = f'{images_dir}\\{i}'
        random.shuffle(all_files)
        return all_files 

    def separation_files(self, all_files: list, folder_sizes: list = [75, 20, 5]):
        total_files = len(all_files)
        train_end = int(total_files * folder_sizes[0] / 100)
        validation_end = int(total_files * folder_sizes[1] / 100) + train_end

        train_files = all_files[:train_end]
        validation_files = all_files[train_end:validation_end]
        test_files = all_files[validation_end:]
        # оставновился на случайном распределении файлов
        return [train_files, validation_files, test_files]

    def move_files(self, folders_path: list, files_names: list):
        for i in range(3): # можно реализовать инумерэйтом
            for j in files_names[i]:
                shutil.move(j, folders_path[i])

    def runer(self, parrent_dir:str, images_dir: str, folder_sizes: list = [75, 20, 5], folder_names: list = ['train', 'validation', 'test']): #, random: bool = False, renaming_picture: bool = False
        '''
        Подумать над тем на сколько нужен ранер
        parrent_dir - the folder in which all actions will take place 
        images_dir - folder containing pictures
        folder_sizes - percentage split into different folders
        folder_names -  folder names to separate
        
        '''
        pis = self.add_folders(parrent_dir, folder_names)
        all_files = self.shuffle_imgs(images_dir)
        al = self.separation_files(all_files, folder_sizes)
        self.move_files(pis, al)
       # FolderManager.remove_old_folder(images_dir)
      