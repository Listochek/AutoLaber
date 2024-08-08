'''Функция для рана всего проекта которая принимает достаточно много параметров'''
import sys
import os
import logging
import sys
sys.path.append("C:/путь_к_вашей_папке")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_management.folder_manager import FolderManager, FolderSeparation
from file_management.remove_duplicates import RemoveDuplicates
from parsing.parse import PictureCrawler
from tests.run_tests import runing_test
from tests.test_set_log import add_logs
from parsing.yolo_auto_prediction import YoloAutoPrediction

def run_ansambl(key_words: list, main_dirr: str, max_pic: int = 2, folders_for_saving: list = ['train\\images', 'validation\\images', 'test\\images'], crawl_mode='Google',remove_duplicates: bool = True):
    '''key_words - лист по которому будет производиться поиск
   main_dir - Дирректория в которой будут создоваться папки с результатами
   folders_for_saving - папки в которые будет распихан датасет предполагается что папок будет только три
   crawler - наименование временной папки которая будет удалена
    '''
    crawler: str = 'Crawler'
    logging.basicConfig(level=logging.INFO, filename="logs\\py_log.log" ,filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    folmg, folsep, pc = FolderManager(), FolderSeparation(), PictureCrawler()

    folmg.remove_old_folder(main_dirr)
    abra = [crawler, *key_words]
    folmg.add_folders(main_dirr, abra)
    pc.run_pars(key_words, main_dirr, max_pic=max_pic, crawl_mode=crawl_mode) #crawl_mode = Google/Bing
    folmg.picture_rename(main_dirr, crawler, folmg.get_all_filenames(main_dirr))
    if remove_duplicates:
        rmd = RemoveDuplicates()
        rmd.find_duplicate_images(folder_path=f'{main_dirr}\\{crawler}', delite_picture=True)
    ab = folmg.add_folders(main_dirr, folders_for_saving)
    sl = folsep.separation_files(folsep.shuffle_imgs(f'{main_dirr}\\{crawler}'))
    folsep.move_files(ab, sl)
    folmg.remove_dirs(main_dirr, [crawler])


def run_yolo_prediction(main_dirr: str,  model: str = 'models\\yolov8n', folders_names: list = ['train', 'validation', 'test'], pic_folders_name: str='images'):
    yp = YoloAutoPrediction(main_dirr=main_dirr, model=model, folders_names=folders_names, pic_folders_name=pic_folders_name)
    yp.run_models()