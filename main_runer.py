'''Функция для рана всего проекта которая принимает достаточно много параметров'''
#from icrawler import BingImageCrawler
import sys
import os
from icrawler.builtin import BingImageCrawler, GoogleImageCrawler
import logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_management.folder_manager import FolderManager, FolderSeparation #RemoveDuplicates
from file_management.remove_duplicates import RemoveDuplicates
from parsing.parse import PictureCrawler
from tests.run_tests import runing_test
from tests.test_set_log import add_logs

#PictureCrawler
# path_to_save = main_dirr
def run_ansambl(key_words: list, main_dirr: str, max_pic: int = 2, folders_for_saving: list = ['train', 'validation', 'test'], crawl_mode='Google', crawler: str = 'Crawler'):
    '''key_words - лист по которому будет производиться поиск
   main_dir - Дирректория в которой будут создоваться папки с результатами
   folders_for_saving - папки в которые будет распихан датасет предполагается что папок будет только три
   crawler - наименование временной папки которая будет удалена
    '''
    logging.basicConfig(level=logging.INFO, filename="py_log.log" ,filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    folmg, folsep = FolderManager(), FolderSeparation()
    pc, rmd = PictureCrawler(), RemoveDuplicates()

    #сделать так чтоб не ремувалась вся папка файлов а только наши файлы
    folmg.remove_old_folder(main_dirr)
    abra = [crawler, *key_words]
    folmg.add_folders(main_dirr, abra)
    # реализовать файл с разгными функциями для скачивания которые будут настроенны чтоб не вызывать через цикл
    # реализвать скачивание через потоки
    # реализвовать класс содержащий парсеры
    pc.run_pars(key_words, main_dirr, max_pic=max_pic, crawl_mode=crawl_mode) #crawl_mode = Google/Bing
    
    folmg.piture_rename(main_dirr, crawler, folmg.get_all_filenames(main_dirr))
    rmd.find_duplicate_images(folder_path=f'{main_dirr}\\{crawler}', delite_picture=True)
    # объеденить после создания вместе с folders_for_saving тк ремувается вся dirra
    ab = folmg.add_folders(main_dirr, folders_for_saving)
    #присоеденить функцию для удаления дубликатов и все это дело
    sl = folsep.separation_files(folsep.shuffle_imgs(f'{main_dirr}\\{crawler}'))
    folsep.move_files(ab, sl)
    folmg.remove_dirs(main_dirr, [crawler])


KEYS = ['котики', 'мышки', 'люди', 'зонтики']
PICTURE_COUNT = 55
run_ansambl(KEYS, 'picture', max_pic=PICTURE_COUNT)
runing_test(KEYS, 'picture', max_pic=PICTURE_COUNT)

'''KEYS = ['котики', 'мышки', 'люди', 'зонтики']
for i in range(50, 80, 5):
    print(f'iteration now: {i}')
    run_ansambl(KEYS, 'picture', max_pic=i)
    runing_test(KEYS, 'picture', max_pic=i)'''