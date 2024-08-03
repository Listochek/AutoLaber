'''Функция для рана всего проекта которая принимает достаточно много параметров'''
#from icrawler import BingImageCrawler
import sys
import os
from icrawler.builtin import BingImageCrawler, GoogleImageCrawler

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_management.folder_manager import FolderManager, FolderSeparation
from parsing.parse import PictureCrawler
#PictureCrawler
# path_to_save = main_dirr
def run_ansambl(key_words: list, main_dirr: str, max_pic: int = 2, folders_for_saving: list = ['train', 'validation', 'test'], crawler: str = 'Crawler'):
    '''key_words - лист по которому будет производиться поиск
   main_dir - Дирректория в которой будут создоваться папки с результатами
   folders_for_saving - папки в которые будет распихан датасет предполагается что папок будет только три
   crawler - наименование временной папки которая будет удалена
    '''
    folmg, folsep = FolderManager(), FolderSeparation()
    pc = PictureCrawler()

    #сделать так чтоб не ремувалась вся папка файлов а только наши файлы
    folmg.remove_old_folder(main_dirr)
    abra = [crawler, *key_words]
    folmg.add_folders(main_dirr, abra)
    # реализовать файл с разгными функциями для скачивания которые будут настроенны чтоб не вызывать через цикл
    # реализвать скачивание через потоки
    # реализвовать класс содержащий парсеры
    pc.run_pars(key_words, main_dirr, max_pic=5)
    folmg.piture_rename(main_dirr, crawler, folmg.get_all_filenames(main_dirr))
    # объеденить после создания вместе с folders_for_saving тк ремувается вся dirra
    ab = folmg.add_folders(main_dirr, folders_for_saving)
    #присоеденить функцию для удаления дубликатов и все это дело
    sl = folsep.separation_files(folsep.shuffle_imgs(f'{main_dirr}\\{crawler}'))
    folsep.move_files(ab, sl)
    folmg.remove_dirs(main_dirr, [crawler])

''' for i in key_words:
        g = GoogleImageCrawler()
        g.__init__(storage={'root_dir': f'{main_dirr}/{i}'})
        g.crawl(keyword=i, max_num=max_pic, file_idx_offset=0)
        #bing_crawler = BingImageCrawler(storage={'root_dir': f'{main_dirr}/{i}'})
        #bing_crawler.crawl(keyword=i, max_num=max_pic, file_idx_offset=0)
        #del bing_crawler
        del g'''

    #почистить папки после переноса
  
KEYS = ['котики', 'мышки', 'коты']
run_ansambl(KEYS, 'picture')


