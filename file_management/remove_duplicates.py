import hashlib
from collections import defaultdict
import os

class RemoveDuplicates():
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
