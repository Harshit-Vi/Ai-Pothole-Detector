"""Logging configuration and setup."""
import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file=None, log_level=None):
    """Setup logger with both file and console handlers.
    
    Args:
        name: Logger name
        log_file: Log file path
        log_level: Logging level
        
    Returns:
        Configured logger instance
    """
    if log_file is None:
        log_file = os.getenv('LOG_FILE', 'logs/app.log')
    
    if log_level is None:
        log_level = os.getenv('LOG_LEVEL', 'INFO')
    
    # Ensure logs directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level))
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, log_level))
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    
    # File handler
    file_handler = RotatingFileHandler(
        log_file, maxBytes=10485760, backupCount=10
    )
    file_handler.setLevel(getattr(logging, log_level))
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(file_formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger
