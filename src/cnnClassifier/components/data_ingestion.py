import os
import zipfile
import gdown
from src.cnnClassifier import logger
from src.cnnClassifier.utils.common import get_size
from src.cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_data(self) -> str:
        try:
            dataset_url = self.config.source_url
            zip_download_dir = str(self.config.local_data_file)
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = str(dataset_url).split("/")[-2]

            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix + file_id, zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        try:
            with zipfile.ZipFile(self.config.local_data_file,'r') as f:
                f.extractall(unzip_path)
                logger.info(f"Extracting the dataset file into the file directory {unzip_path}")
        except Exception as e:
            raise e
    
    