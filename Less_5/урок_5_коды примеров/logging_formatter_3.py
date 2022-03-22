"""
Журналирование (логгирование) с использованием модуля logging
Расширенная настройка. Форматирование, обработчики
"""

import logging

# Создать логгер - регистратор верхнего уроовня
# с именем app.main
import os.path

LOG = logging.getLogger('app.main')

# Создать обработчик
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'app.log')
FILE_HANDLER = logging.FileHandler(PATH, encoding='utf-8')
# выводит сообщения с уровнем DEBUG
FILE_HANDLER.setLevel(logging.DEBUG)

# Создать объект Formatter
# Определить формат сообщений
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

# подключить объект Formatter к обработчику
FILE_HANDLER.setFormatter(FORMATTER)

# Добавить обработчик к регистратору
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)

# Передать сообщение обработчику
# LOG.info('Информационное сообщение')

if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.warning('Предупреждения')
    LOG.info('Информационное сообщение')
    LOG.debug('Отладочная информация')
