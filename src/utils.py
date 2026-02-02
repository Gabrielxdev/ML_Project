import os 
import sys 
import numpy as np 
import pandas as pd 
import dill #É uma biblioteca mais poderosa que o pickle (famoso no Python) para salvar coisas complexas.
from src.exception import CustomException 


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path) 
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj: #precisamos salvá-lo como uma sequência de bytes (zeros e uns). Se usasse apenas "w", daria erro.
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e, sys)