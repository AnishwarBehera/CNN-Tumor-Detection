import tensorflow as tf
from src.cnnClassifier.entity.config_entity import EvaluationConfig
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.utils.common import load_model,save_score,save_json
from  urllib.parse import urlparse  
import keras
from pathlib import Path


class Evaluation:
    def __init__(self,config:EvaluationConfig):
        self.config=config

    def valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.25
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    def evaluation(self):
        self.model= load_model(self.config.path_to_model)
        self.valid_generator()
        self.score= self.model.evaluate(self.valid_generator)
        save_score(self.score)


    # def save_score(self):
    #     scores={"loss": self.score[0], "accuracy": self.score[1]}
    #     save_json(path=Path(self.config.root_dir),data=scores)