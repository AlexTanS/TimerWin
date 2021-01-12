"""
Программа по таймеру оповещает о том, что необходимо сделать (работать, отдыхать и т.д.)
Предыдущие состяния программы и настройки хранятся в отдельном файле.
"""
from os import environ

# Константы
# ====================================================================================================================
SETTING_FILE = "setting_timer_win.txt"  # имя файла с настройками программы


# Функции
# ====================================================================================================================
def check_file_config():
    """ Проверяет есть ли файлы с настройками, если нету - создает его."""
    pass


def get_path_user_docs() -> str:
    """ Получение переменной, указывающей путь к файлу с настройками в директории 'Документы'."""
    global SETTING_FILE
    p = environ['USERPROFILE'] + "\\Documents\\" + SETTING_FILE
    return p


if __name__ == '__main__':
    print(get_path_user_docs())
