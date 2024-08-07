import sys
sys.path.append("autolaber") # путь до скаченного репозитория

from autolaber import run_ansambl, runing_test, run_yolo_prediction

KEY_WORDS = ['cats', 'dogs', 'bird'] # лист слов для скачивания картинок
main_dirr = 'picture' # папка в которой будут происходить все действия
# ПРИ РАБОТЕ main_dir ПОЛНОСТЬЮ УДАЛЯЕТСЯ БУДЬТЕ ОСТОРОЖНЫ
MAX_PIC = 3 # колличество картинок для скачивания
folders_for_saving = ['train\\images', 'validation\\images', 'test\\images'] 
# папки для сохранения картинок, создадутся в main_dir (установленны зарание)
crawl_mode = 'Google' # есть два моды парсинга Google/Bing
remove_duplicates = True # удалять ли дубликаты картинок

run_ansambl(
    key_words=KEY_WORDS,
    main_dirr=main_dirr,
    max_pic=MAX_PIC,
    folders_for_saving= folders_for_saving,
    crawl_mode=crawl_mode,
    remove_duplicates=remove_duplicates
)


main_dirr='picture' # используется таже дирректория что и для парсинга
model = 'models\\yolov8n' # для примера используем yolov8n, можите подключить свою модель
# Бибилиотека заточена на работу с модели YOLO 8+ серии
#folders_names = ['train', 'validation', 'test'], # если вы не меняли folders_for_saving то менять ничего не нужно
pic_folders_name = 'images' # pic_folders_name должен стоятб такой же как в конце путей folders_for_saving=[train\\images...]
folders_names = ['train', 'validation', 'test']
run_yolo_prediction(main_dirr=main_dirr, model=model, pic_folders_name=pic_folders_name, folders_names=folders_names)
'''run_ansambl(KEYS, 'picture', max_pic=PICTURE_COUNT)
run_yolo_prediction(main_dirr='picture')
runing_test(KEYS, 'picture', max_pic=PICTURE_COUNT)
'''
    