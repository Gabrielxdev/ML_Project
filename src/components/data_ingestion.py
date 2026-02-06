# Este código é responsável por fazer a ingestão de dados, ou seja, extrair
import os 
import sys #o "inspetor" do código: ele sabe tudo o que está acontecendo nos bastidores da execução.
from src.exception import CustomException
from src.logger import logging 
import pandas as pd 

from sklearn.model_selection import train_test_split 
from dataclasses import dataclass  # Uma ferramenta do Python que facilita a criação de classes que servem apenas para guardar dados (configurações), sem precisar escrever métodos como __init__.
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainer 
from src.components.model_trainer import ModelTrainerConfig 


@dataclass #Um decorador que cria automaticamente o método construtor (__init__) para a classe abaixo.

class DataIngestionConfig: #Define os caminhos onde os arquivos serão salvos.
    train_data_path: str=os.path.join("artifacts", "train.csv")
    test_data_path: str=os.path.join("artifacts", "test.csv")
    raw_data_path: str=os.path.join("artifacts", "data.csv") #os arquivos train.csv, test.csv e data.csv (bruto) ficarão dentro de uma pasta chamada artifacts.

class DataIngestion: #Classe que vai fazer a ingestão de dados.
    def __init__(self): 
        self.ingestion_config = DataIngestionConfig() #Cria uma instância da configuração (DataIngestionConfig), para que o código saiba onde salvar os arquivos.


    def initiate_data_ingestion(self): 
        logging.info("Entered the data ingestion method or component") #Registra no log que o processo de ingestão começou. Útil para debug.
        try:
            df = pd.read_csv('notebook/data/stud.csv') #Leitura do arquivo CSV.

            logging.info("Read the dataset as dataframe") #Registra no log que o dataset foi lido e convertido para um DataFrame.

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) #Pega apenas o diretório do caminho do arquivo de treino (ou seja, pega "artifacts").
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True) #Salva o DataFrame como um arquivo CSV.

            logging.info("Train test split initiated") #Registra no log que o processo de split começou.

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42) #Divide o DataFrame em conjuntos de treinamento e teste.
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True) #Salva o conjunto de teste como um arquivo CSV.
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True) #Salva o conjunto de treinamento como um arquivo CSV.

            logging.info("Ingestion of data is completed") #Registra no log que o processo de ingestão terminou.

            return (
            self.ingestion_config.train_data_path, #Retorna o caminho do arquivo de treino.
            self.ingestion_config.test_data_path #Retorna o caminho do arquivo de teste.
            )
        except Exception as e: #Lança o erro usando sua classe personalizada, que provavelmente adiciona informações como nome do arquivo e número da linha onde o erro ocorreu.
            raise CustomException(e, sys)
if __name__ == "__main__": #Ela pergunta: "Este arquivo (data_ingestion.py) está sendo executado diretamente pelo terminal (ex: python data_ingestion.py)?"
    obj=DataIngestion() #Se sim, ele cria uma instância da classe DataIngestion.
    train_data, test_data = obj.initiate_data_ingestion() #E executa o método initiate_data_ingestion().

    #conclusão: Esse método vai ler o dataset original, dividir em treino/teste e salvar os arquivos .csv na pasta artifacts.
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    modelTrainer = ModelTrainer()
    print(modelTrainer.initiate_model_trainer(train_arr, test_arr))