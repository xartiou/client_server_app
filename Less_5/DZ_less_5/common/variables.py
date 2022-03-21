"""Константы используемые в коде"""
import logging
# Порт по умолчанию для сетевого взаимодействия
DEFAULT_PORT = 7777
# IP адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 5
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
ENCODING = 'utf-8'

# Протокол JIM основные ключи:
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'

# Прочие ключи, используемые в протоколе
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
RESPONDEFAULT_IP_ADDRESSSE = 'respondefault_ip_addressse'

# для теста
OK_DICT = {RESPONSE: 200}
ERROR_DICT = {RESPONSE: 400, ERROR: 'Bad Request'}
ERROR_DICT_SERVER = {ERROR: 'Bad Request', RESPONDEFAULT_IP_ADDRESSSE: 400}
DICT_SEND = {ACTION: PRESENCE, TIME: 1, USER: ACCOUNT_NAME}

# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG
