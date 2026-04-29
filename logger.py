import logging

logger = logging.getLogger('roblox_tools')
logger.setLevel(logging.INFO)

# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to ch
ch.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(ch)

def log_info(message: str) -> None:
    """Logs an informational message."""
    logger.info(message)


def log_error(message: str) -> None:
    """Logs an error message."""
    logger.error(message)


def log_warning(message: str) -> None:
    """Logs a warning message."""
    logger.warning(message)


def log_debug(message: str) -> None:
    """Logs a debug message."""
    logger.debug(message)
