import logging


class Logger:
    """A simple logger for Roblox tools."""

    def __init__(self, name: str) -> None:
        """Initializes the Logger with a name."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message: str) -> None:
        """Logs a message with DEBUG level."""
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """Logs a message with INFO level."""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Logs a message with WARNING level."""
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """Logs a message with ERROR level."""
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """Logs a message with CRITICAL level."""
        self.logger.critical(message)