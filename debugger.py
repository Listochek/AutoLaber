from autolaber import run_ansambl, runing_test, run_yolo_prediction

KEYS = ['котики', 'cats']
PICTURE_COUNT = 3
#run_ansambl(KEYS, 'picture', max_pic=PICTURE_COUNT)
#run_yolo_prediction(main_dirr='picture')
runing_test(KEYS, 'picture', max_pic=PICTURE_COUNT)

    