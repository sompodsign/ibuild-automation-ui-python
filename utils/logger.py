
from loguru import logger


class CustomLogger:
    """
    Custom logger class to be used in the project to get beautiful logs for every steps on tests.
    """

    def __init__(self, log_file_name):
        self.logger = logger
        self.logger.add(f"logs/{log_file_name}.log", format="{time} {level} {message}", mode="w")

    def get_logger(self):
        return self.logger

    # def info(self, message):
    #     return self.logger.info("✔ " + message)
    #
    # def error(self, message):
    #     return self.logger.error("✘ " + message)
