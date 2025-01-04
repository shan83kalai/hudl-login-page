import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Adjust to DEBUG for development
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)
