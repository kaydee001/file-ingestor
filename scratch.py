import logging


class PrintHandler(logging.Handler):
    def emit(self, record):
        print("Message:", record.getMessage())
        print("Level:", record.levelname)
        print("Filename:", record.filename)   # new line


logger = logging.getLogger("test")
logger.addHandler(PrintHandler())
logger.setLevel(logging.INFO)

logger.info("file checked", extra={"filename": "test.png"})
