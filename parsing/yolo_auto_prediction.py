from ultralytics import YOLO
import os
import shutil
class YoloAutoPrediction:
    '''в initе принимает модель, словарь классов
    main_dir в которой будет папки [train, validation, test] в каждой папке будет images/labels
    
    
    main_logics: YoloPredicts -> ([bbox], [cls]), fun(bbox -> yolo_bbox) -> {cls: [bbox]} -> label
    '''
    def __init__(self, main_dirr: str,  model: str = 'models\\yolov8n', folders_names = ['train', 'validation', 'test'], pic_folders_name='images'):
        self.folders_names = folders_names
        self.main_dirr = main_dirr
        self.model = YOLO(model=model)
        self.pic_folders_name = pic_folders_name

    def run_models(self): # переименовать функцию
        paths = self.get_image_paths(self.main_dirr)
        for i in paths:
          self.prediction(path_to_pic=i, model=self.model)
        mb_prediction_runs = 'runs\\detect\\predict\\labels'
        kon = self.get_text_paths(mb_prediction_runs)
        self.add_folders(main_dirr=self.main_dirr, folders_names=self.folders_names, fold_name='labels')
        r = self.add_path_txt(path_to_pic=paths)
        al = self.search_pair(kon, r)
        self.move_txt(al)

    def prediction(self, path_to_pic: list, model, conf: float = 0.5, imgsz: int = 320):
        model.predict(path_to_pic, imgsz=imgsz, conf=conf, save_txt=True)

    def get_image_paths(self, directory: str) -> list:
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}  # Можно добавить другие расширения
        image_paths = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.lower().endswith(ext) for ext in image_extensions):
                    image_paths.append(os.path.join(root, file))

        return image_paths
    def get_text_paths(self, path_to_txt: str) -> list:
        # Получаем полные пути к файлам в указанной директории
         return [os.path.join(path_to_txt, filename) for filename in os.listdir(path_to_txt)]
    #model.predict(source, imgsz=320, conf=0.5, save_txt=True)
    def add_folders(self, main_dirr: str, folders_names: list = ['train', 'validation', 'test'], fold_name: str = 'labels') -> None:
            # Создание необходимых папок
            for folder in folders_names:
                # Путь к директории
                folder_path = os.path.join(main_dirr, folder, fold_name)
                try:
                    os.makedirs(folder_path, exist_ok=True)  # Создает директорию и не вызывает ошибку, если она уже существует
                    print(f"Создана директория: {folder_path}")
                except Exception as e:
                    print(f"Ошибка при создании директории {folder_path}: {e}")

    def add_path_txt(self, path_to_pic: list, pic_folders_name: str = 'images') -> list:
        path_txt = []
        for i in path_to_pic:    
            a = i.replace(pic_folders_name, 'labels')
            path_txt.append(a.replace('.jpg', '.txt'))
        return path_txt

    def search_pair(self, path_to_txt_1: list, path_to_txt_2:list) -> list:
        pair_lst = []
        for i in path_to_txt_1:
            path_1 = i.split('\\')
        
            for j in path_to_txt_2:
                if path_1[-1] in j:
                    pair_lst.append((i, j))
        return pair_lst
    
    def move_txt(self, path_pair_list: list):
        for i in path_pair_list:
            dest_dir = os.path.dirname(i[1])
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            try:
                shutil.move(i[0], i[1])
            except Exception as e:
                print(f"Ошибка при перемещении файла {i[0]} в {i[1]}: {e}")
#a = search_pair()
#print(a)
# Пример использования
'''yp = YoloAutoPrediction(main_dir='picture')
yp.run_models()'''