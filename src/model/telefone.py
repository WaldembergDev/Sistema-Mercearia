class Telefone:
    def __init__(self, id_telefone, telefone):
        self.id_telefone = id_telefone
        self.telefone = telefone


class TelefoneCliente(Telefone):
    def __init__(self, id_telefone, telefone, cliente_id):
        super().__init__(id_telefone, telefone)
        self.cliente_id = cliente_id


class TelefoneFuncionario(Telefone):
    def __init__(self, id_telefone, telefone, funcionario_id):
        super().__init__(id_telefone, telefone)
        self.funcionario_id = funcionario_id