
from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.prepare_base_model_pipeline import PrepareBaseModelPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.initiate_data_ingestion()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare base model"
try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.initiate_prepare_base_model()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e   