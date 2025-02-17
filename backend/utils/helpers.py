"""
Provides helper functions for logging, text processing, and API responses.
"""

import logging

#Configure logging format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers = [logging.StreamHandler()]
)

def log_message(message: str, level: str="info"):
    """
    Logs messages at various severity levels
    """

    if level =="info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    elif level == "debug":
        logging.debug(message)
    
def clean_text(text: str) -> str:
    """
    Cleans input text
    """
    return text.strip().replace("\n"," ")

def format_response(data, message="Success"):
    """
    Formats API responses in a structured JSON format.
    """
    return{
        "status": "success",
        "message": message,
        "data": data
    }


