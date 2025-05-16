import logging

LOGGER = logging.getLogger(__name__)
FILE_LOGGER = logging.getLogger(__name__)

"""The StreamHandler class will send your logs to the console. The FileHandler class writes your log records to a 
file. To define where and how you want to write the logs, you provide a file path, an opening mode, and the encoding."""


console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
LOGGER.addHandler(console_handler)
FILE_LOGGER.addHandler(file_handler)
LOGGER.level = logging.DEBUG
formatter = logging.Formatter(
    "{asctime}s - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
)
FILE_LOGGER.level = logging.DEBUG

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
