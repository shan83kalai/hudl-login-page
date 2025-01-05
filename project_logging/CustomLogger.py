import logging

# Setup custom logger
logger = logging.getLogger("hudl_test_logger")
logger.setLevel(logging.INFO)  # Set logging level to INFO

# Avoid adding multiple handlers if logger already has handlers
if not logger.handlers:
    # Create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Set log format
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)
