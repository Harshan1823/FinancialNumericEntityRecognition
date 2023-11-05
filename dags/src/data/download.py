
def download_and_store_data(DATASET_NAME: str, logger, root_dir):
    import datasets
    import pandas as pd
    import os
    from pathlib import Path
    import sys
    # setup_logger('download_data')
    logger = logger
    splits = ["train", "validation", "test"]
    logger.info("Starting the download process")
    DESTINATION_FOLDER = root_dir / 'data' / 'raw'
    try:
        # Save each split as CSV
        for split in splits:
            filepath = DESTINATION_FOLDER / f"{split}.csv"
            logger.info(f"File Path: {filepath}")
            if filepath.exists():
                logger.info(f"{split}.csv already exists at {filepath}. Skipping download.")
                continue
            logger.info(f"Trying to download {split} data")
            logger.info(f"{split} data will be saved to {filepath}")
            data = datasets.load_dataset(DATASET_NAME, split=split)
            df = pd.DataFrame(data)
            df.to_csv(filepath, index=False)
            logger.info(f"{split} data saved to {filepath}")
            logger.info(f"Downloaded {split} data")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
