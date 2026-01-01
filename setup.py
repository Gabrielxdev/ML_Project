from setuptools import find_namespace_packages, setup 
from typing import List

Hypen_E_Dot = "-e ."
def get_requirements(file_path:str)->List[str]: #retornar uma List (lista) onde cada item dentro dela é uma str (string).
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file_obj: #é um gerenciador de contexto. Ele abre o arquivo e garante que ele seja fechado automaticamente assim que o bloco de código terminar (ou se der algum erro).
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] #"Substitua toda vez que encontrar \n por "" (vazio)." Basicamente, isso apaga a quebra de linha.

        if Hypen_E_Dot in requirements: #Se ele encontrar o texto "-e ." em requirements.txt, ele vai tentar baixar um pacote com esse nome da internet e vai falhar, pois isso não é um pacote, é apenas uma configuração.
            requirements.remove(Hypen_E_Dot) #Remove o texto "-e ." da lista requirements.
    return requirements
    
setup (
    name="ML_Project",
    version="0.0.1",
    packages=find_namespace_packages(),
    author="Gabriel",
    author_email="leucides123@gmail.com",
    install_requires=get_requirements("requirements.txt")
)