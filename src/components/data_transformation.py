import sys # Importa o sistema para acessar informações do interpretador
from dataclasses import dataclass 
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import ColumnTransformer 
from sklearn.pipeline import Pipeline 
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException 
from src.logger import logging 
import os 

@dataclass 
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig() 

    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity", 
                "parental_level_of_education", 
                "lunch",
                "test_preparation_course"
            ]
        
        num_pipeline = Pipeline(
            steps = [
                ("imputer", SimpleImputer(strategy="median")), # Substitui valores faltantes pela mediana
                ("scaler", StandardScaler()) # Escala os dados para ter média 0 e desvio padrão 1
            ]
        )

        cat_pipeline = Pipeline (
            steps = [
                ("imputer", SimpleImputer(strategy="most_frequent")), # Substitui valores faltantes pela moda
                ("one_hot_encoder", OneHotEncoder()), # Codifica as variáveis categóricas
                ("scaler", StandardScaler())
            ]
        )
        logging.info("Numerical columns standard scaling completed")
        logging.info("Categorical columns encoding completed")

        preprocessor = ColumnTransformer(
            [
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipelines", cat_pipeline, categorical_columns)
            ]
        )

        return preprocessor 

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()
            target_column_name="math_score"
        except:
            pass