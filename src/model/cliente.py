from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, id_cliente, nome, cpf, data_nascimento, email, endereco_id, data_cadastro):
        super().__init__(nome, cpf, data_nascimento, email, endereco_id)
        self.id_cliente = id_cliente
        self.data_cadastro = data_cadastro