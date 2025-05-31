class Pessoa:
    def __init__(self, id_pessoa, nome):
        self.id_pessoa = id_pessoa
        self.nome = nome

class Telefone:
    def __init__(self, id_telefone, telefone, id_pessoa):
        self.id_telefone = id_telefone
        self.telefone = telefone
        self.id_pessoa = id_pessoa

def buscar_nome_por_telefone(id_telefone, telefones, pessoas):
    if id_telefone in telefones:
        id_pessoa = telefones[id_telefone].id_pessoa
        return pessoas.get(id_pessoa, Pessoa(None, "Não encontrado")).nome
    return "Telefone não encontrado"

# Criando os dados
pessoas = {
    "P1": Pessoa("P1", "Lucas Venezian Povoa"),
    "P2": Pessoa("P2", "Ana Carla Rossinholi Venezian")
}

telefones = {
    "T1": Telefone("T1", "112233", "P1"),
    "T2": Telefone("T2", "223344", "P2")
}

# Entrada do usuário
id_telefone = input("Digite o ID do telefone: ")
nome_pessoa = buscar_nome_por_telefone(id_telefone, telefones, pessoas)
print("Nome associado:", nome_pessoa)
