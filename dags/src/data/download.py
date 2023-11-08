
def download_and_store_data(DATASET_NAME: str, logger, root_dir):
    
    """
    Downloads data from a specified dataset, splits it into train, validation, and test sets, and stores them as CSV files.

    This function uses the 'datasets' library to download data from the specified dataset. It then splits the data into three
    subsets (train, validation, and test) and saves each subset as a CSV file in the 'data/raw' directory located in the
    'root_dir'. If a subset CSV file already exists, it skips the download for that subset.

    :param DATASET_NAME: A string representing the name of the dataset to be downloaded.
    :param logger: A logger object for logging messages and errors.
    :param root_dir: A Path object representing the project's root directory.

    :raises: Exception if an error occurs during the download and storage process.
    """
    
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
            data = datasets.load_dataset(DATASET_NAME, split=split) # Download data for the specified split
            df = pd.DataFrame(data)
            df.to_csv(filepath, index=False) # Save the data as a CSV file
            logger.info(f"{split} data saved to {filepath}")
            logger.info(f"Downloaded {split} data")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
