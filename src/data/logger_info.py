import logging
import logging.handlers
from pathlib import Path

def setup_logger(name):
    # Determine the project root and log directory
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    log_dir = PROJECT_ROOT / 'logs'
    log_filepath = log_dir / 'app.log'  # The path for the log file

    # Ensure the logs directory exists
    log_dir.mkdir(parents=True, exist_ok=True)

    # Set up logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(console_formatter)
    logger.addHandler(ch)

    # File handler
    fh = logging.handlers.RotatingFileHandler(
        log_filepath, maxBytes=10*1024*1024, backupCount=3  # 10MB per file, keep last 3 logs
    )
    fh.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(file_formatter)
    logger.addHandler(fh)

    return logger
