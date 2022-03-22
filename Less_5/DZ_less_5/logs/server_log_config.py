"""Кофнфиг серверного логгера"""

import sys
import os
import logging
import logging.handlers
# sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append('../')
from common.variables import LOGGING_LEVEL

# создаём формировщик логов (formatter):
# # "<дата-время> <уровеньважности> <имямодуля> <сообщение>"
SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)-10s %(filename)s %(message)s')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

# создаём потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
# На стороне сервера необходимо настроить ежедневную ротацию лог-файлов.
# class logging.handlers.TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None,
# delay=False, utc=False, atTime=None, errors=None)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', when='D', interval=1 )
LOG_FILE.setFormatter(SERVER_FORMATTER)

# создаём регистратор и настраиваем его
LOGGER = logging.getLogger('server')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.warning('Предупреждения')
    LOGGER.info('Информационное сообщение')
    LOGGER.debug('Отладочная информация')
