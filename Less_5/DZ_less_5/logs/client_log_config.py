"""Конфиг клиентского логгера"""

import sys
import os
import logging
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import LOGGING_LEVEL

# создаём формировщик логов (formatter):
# "<дата-время> <уровеньважности> <имямодуля> <сообщение>"
CLIENT_FORMATTER = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)s %(message)s')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

# создаём потоки вывода логов
# in stream
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)
# уровень для in stream
STREAM_HANDLER.setLevel(logging.INFO)
# in file
LOG_FILE = logging.FileHandler(PATH, encoding='utf-8')
LOG_FILE.setFormatter(CLIENT_FORMATTER)

# создаём регистратор и настраиваем его
# объеденяем работу logging.Formatter и logging.StreamHandler, logging.FileHandler
LOGGER = logging.getLogger('client')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
# устанавливаем общий уровень
LOGGER.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.warning('Предупреждения')
    LOGGER.info('Информационное сообщение')
    LOGGER.debug('Отладочная информация')
