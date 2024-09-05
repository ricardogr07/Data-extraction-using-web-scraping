import logging
class Logger:
    """
    A class for logging messages to a file and the console.

    Args:
        filename (str): The name of the log file.

    Attributes:
        log (logging.Logger): The logger object.

    """

    def __init__(self, filename: str):
        """
        Initializes a new instance of the Logger class.

        Args:
            filename (str): The name of the log file.

        """
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        self.log = logging.getLogger()
        self.log.addHandler(stream_handler)
