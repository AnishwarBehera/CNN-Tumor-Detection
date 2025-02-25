from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.model_evaluation import Evaluation
from src.cnnClassifier import logger




STAGE_NAME='Evaluation Stage'

class EvaluationPipeline:
    def __init__(self) -> None:
        pass
    
    def initiate_evaluation(self):
        config=ConfigurationManager()
        eval_config=config.get_evaluation_config()
        evaluation=Evaluation(eval_config)
        evaluation.evaluation()
        
    

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.initiate_evaluation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
