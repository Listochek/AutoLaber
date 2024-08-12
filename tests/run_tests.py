import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.test_set_log import add_logs
from tests.main_test import check_images, image_weight, broken_pictures, find_duplicate_images, get_image_sizes, repeating_size_counter
from file_management.folder_manager import FolderManager
import logging



def runing_test(key_words: list, main_dirr: str, max_pic: int = 2, folders_for_saving: list = ['train\\images', 'validation\\images', 'test\\images']):
    # -- logs -- #
    logging.basicConfig(level=logging.INFO, filename="logs\\test_log.log" ,filemode="w", format="%(asctime)s %(levelname)s %(message)s")
    from tests.test_set_log import add_logs
    logger = add_logs()

    # -- logs -- #
    flm = FolderManager()
    path_to_images = flm.get_filenames_in_dirrectores(dirr=main_dirr, folders=folders_for_saving) 
    logger.test(f'check_images: {check_images(pic_list=path_to_images, key_words=key_words, max_pic=max_pic)}')
    logger.test(f'image_weight: {image_weight(path_to_images)}')
    logger.test(f'broken images: {broken_pictures(path_to_images)}')

