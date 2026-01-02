import logging # é usada para registrar mensagens de log em seu código, ajudando você a rastrear e depurar problemas.
import os # fornece funcionalidades para interagir com o sistema operacional, como criar diretórios e arquivos.
from datetime import datetime # fornece funcionalidades para trabalhar com datas e horas.

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # cria uma string para o nome do arquivo, pega a data compelta e hora atual.
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # cria uma string para o caminho do arquivo. Exemplo: "logs/01_01_2026_23_21_31.log"

logging.basicConfig( #configura o logging para registrar as mensagens de log.
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # ai aparecer: [Data e Hora] Número da Linha Nome do Logger - Nível (Info/Error) - A mensagem.
    level=logging.INFO, # define o nível de logging. significa que mensagens de informação geral, avisos e erros serão salvos, mas mensagens de "DEBUG" não.
)



    # logger.py cria um histórico de logs de tudo que acontece 
    # durante a execução do código, ajudando a rastrear e depurar problemas.
    # Ele registra informações úteis como o nome do arquivo, número da linha e o nível do erro.