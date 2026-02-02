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

@dataclass #automatiza metodos criados em classes que servem apenas para guardar dados
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl") 

class DataTransformation: # é o molde que vai transformar os dados 
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig() #cria uma instância da configuração (DataTransformationConfig), para que o código saiba onde salvar os arquivos.

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
                    ("scaler", StandardScaler()) # Escala os dados para ter média 0 e desvio padrão 1
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
            return preprocessor  #retorna o preprocessor 
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object() #chama o método get_data_transformer_object() para obter o preprocessor.

            target_column_name="math_score" #define o nome da coluna alvo.

            input_feature_train_df = train_df.drop(columns=[target_columns_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training and test data")

            input_feature_train_arr =  preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)] #concatena os arrays de entrada e alvo
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)] #concatena os arrays de entrada e alvo

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )

            return (
                train_arr, 
                test_arr, 
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except:
            pass #se der erro, ele passa.