import os
import tensorflow as tf
from src.cnnClassifier.entity.config_entity import PrepareBaseModelConfig
from src.cnnClassifier.utils.common import save_model
from tensorflow.keras.metrics import Precision, Recall
# from tensorflow.keras.applications import ResNet50



class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.applications.ResNet50(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )
        save_model(path=self.config.base_model_path, model=self.model)
    
    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate, dropout_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = True

        flatten_in = tf.keras.layers.Flatten()(model.output)
        dense_layer = tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.001))(flatten_in)
        batch_norm_layer = tf.keras.layers.BatchNormalization()(dense_layer)
        dropout_layer = tf.keras.layers.Dropout(dropout_rate)(batch_norm_layer)

        prediction = tf.keras.layers.Dense(units=classes, activation="softmax")(dropout_layer)

        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)

        full_model.compile(
            optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy", Precision(name="precision"), Recall(name="recall")]
        )

        full_model.summary()
        print(full_model.summary())
        return full_model
    
    def update_base_model(self):
        self.full_model = self.prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,  
            freeze_all=False,
            freeze_till=5,
            learning_rate=self.config.params_learning_rate,
            dropout_rate=self.config.params_dropout_rate
        )

        save_model(path=self.config.updated_base_model_path, model=self.full_model)
