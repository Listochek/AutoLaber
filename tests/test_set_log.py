import logging

def add_logs():


    MY_CUSTOM_LEVEL = 45  # Уровень выше WARNING (30) и ниже INFO (20)
    logging.addLevelName(MY_CUSTOM_LEVEL, "TEST")
    def test(self, message, *args, **kwargs):
        if self.isEnabledFor(MY_CUSTOM_LEVEL):
            self._log(MY_CUSTOM_LEVEL, message, args, **kwargs)
    # 2. Определяем функцию для использования нового уровня

    logging.basicConfig(level=logging.INFO, filename="logs\\test_log.log" ,filemode="a", format="%(asctime)s %(levelname)s %(message)s")

    # Добавляем новый метод в класс Logger
    logging.Logger.test = test
    logger = logging.getLogger(__name__)
    return logger