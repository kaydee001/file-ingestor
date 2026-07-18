import logging


class JSONFileHandler(logging.Handler):
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath

    def emit(self, record):
        pass
