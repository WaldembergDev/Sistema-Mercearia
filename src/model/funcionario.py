from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, id_funcionario, nome, cpf, data_nascimento, email, endereco_id, data_contratacao):
        super().__init__(nome, cpf, data_nascimento, email, endereco_id)
        self.id_funcionario = id_funcionario
        self.data_contratacao = data_contratacao