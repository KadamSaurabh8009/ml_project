import logging
import os
from datetime import datetime

# Create a logs folder
logs_dir = os.path.join(os.getcwd(), "logs")
if not os.path.exists(logs_dir):  # works in all Python versions
    os.makedirs(logs_dir)

# Log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [line:%(lineno)d] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

