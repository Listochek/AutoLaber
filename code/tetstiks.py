'''import os
import shutil

if os.path.isdir('TESTS'):
    shutil.rmtree('TESTS')
else:
    print("Directory does not exist")'''

mass = [1, 2, 3]
mass.remove(2)
print(mass)
#print(mass)

'''    def process_duplicates(self, ):
        pass'''
"""
            folder_sizes = [75, 20, 5] 

            75% - pictures on train, 
            20% - pictures on vallidation, 
            5% - pictures on test
        
            random = False

            True - random distribution of pictures
            False - sequential image division
"""  

'''
def bing_list_crawler(key_words: list, Save_path: str, max_pic: int = 1, main_folder_name: str = 'Crawler', synonym: bool = False):
    FolderManager.remove_old_folder(Save_path) # перезаписать для разделения через объект с наследованием
    FolderManager.add_folders(Save_path, key_words)
    os.makedirs(f'{Save_path}\\{main_folder_name}')
    for i in key_words:
        bing_crawler = BingImageCrawler(storage={'root_dir': f'{Save_path}/{i}'})
        bing_crawler.crawl(keyword=i, max_num=max_pic, file_idx_offset=0)
    FolderManager.piture_rename(Save_path, main_folder_name, FolderManager.get_all_filenames(Save_path))
#FolderSeparation.runer()'''