import logging

# Configure logging for debug information
def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(__name__)
    return logger

logger = setup_logging()

def sanitize_input(text: str) -> str:
    """Sanitizes input to prevent injection or other issues."""
    return text.replace(";", "").replace("&", "").strip()
