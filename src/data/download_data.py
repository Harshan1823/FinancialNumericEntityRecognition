import sys
import datasets
from pathlib import Path
import pandas as pd
# Add the root directory of your project to sys.path
root_dir = Path(__file__).resolve().parents[2]
sys.path.append(str(root_dir))

from src.data import DESTINATION_FOLDER, DATASET_NAME
from src.data.logger_info import setup_logger

logger = setup_logger('download_data')
splits = ["train", "validation", "test"]

# Make sure the destination directory exists
DESTINATION_FOLDER.mkdir(parents=True, exist_ok=True)

def download_and_store_data(dataset_name: str):
    try:
        logger.info("Starting the download process")
        # Save each split as CSV
        for split in splits:
            filepath = DESTINATION_FOLDER / f"{split}.csv"
            if filepath.exists():
                logger.info(f"{split}.csv already exists at {filepath}. Skipping download.")
                continue
            logger.info(f"Trying to download {split} data")
            data = datasets.load_dataset(dataset_name, split=split)
            df = pd.DataFrame(data)
            df.to_csv(filepath, index=False)
            logger.info(f"{split} data saved to {filepath}")
            logger.info(f"Downloaded {split} data")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    download_and_store_data(DATASET_NAME)




