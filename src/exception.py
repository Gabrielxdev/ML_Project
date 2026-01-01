import sys # Importa o sistema para acessar informações do interpretador

def error_message_detail(error, error_detail:sys):
    """
    Função auxiliar para formatar a mensagem de erro detalhada.
    """
    # sys.exc_info() retorna (tipo, valor, traceback). Usamos _ para descartar o que não queremos.
    _, _, exc_tb = error_detail.exc_info()

    # Navega nas camadas do objeto de traceback para extrair o nome do script (arquivo)
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Monta uma string formatada com: Nome do Arquivo, Número da Linha e a Mensagem do Erro
    error_message = "Erro no script Python: [{0}] linha: [{1}] mensagem: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    """
    Nossa classe personalizada que herda da classe base Exception do Python.
    """
    def __init__(self, error_message, error_detail:sys):
        """
        CONSTRUTOR: Executado no momento em que você 'levanta' o erro (raise).
        """
        # Chama o construtor da classe pai (Exception) para inicializar o erro padrão
        super().__init__(error_message)

        # Usamos nossa função auxiliar para gerar a mensagem bonitona e detalhada
        # e guardamos ela dentro do objeto (self) para uso futuro.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Define o que aparece quando você dá um print(erro) ou transforma o erro em string.
        """
        return self.error_message