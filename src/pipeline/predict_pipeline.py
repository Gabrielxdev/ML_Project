import pandas as pd 
import sys  
from src.exception import CustomException 
from src.utils import load_object 

class PredictPipeline:
    def __init__(self):
        pass 

    def predict(self, features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)

class CustomData: #Esta classe é responsável por mapear o que vem do site (HTML) para o formato que o Python entende.
    def __init__ ( # # Recebe todos os dados do formulário
        self, 
        gender: str, 
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int, 
        writing_score: int 
    ):

        self.gender = gender ## Guarda o gênero na memória
        self.race_ethnicity = race_ethnicity ## Guarda a raça/etnia na memória
        self.parental_level_of_education = parental_level_of_education ## Guarda o nível de educação dos pais na memória
        self.lunch = lunch ## Guarda o tipo de almoço na memória
        self.test_preparation_course = test_preparation_course ## Guarda o curso preparatório na memória
        self.reading_score = reading_score ## Guarda a nota de leitura na memória
        self.writing_score = writing_score ## Guarda a nota de escrita na memória

    def get_data_as_dataframe(self):

        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)




