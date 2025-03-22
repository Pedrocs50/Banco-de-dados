class Pessoa:
    def __init__(self, cpf, nome):
        self._cpf = cpf
        self._nome = nome

    def __str__(self):
        return f'CPF = {self._cpf} | Nome = {self._nome}'

class Tabela_Pessoa(Pessoa):   
    def Tabela_Pessoa(self):
        return f'CPF = {self._cpf} | Nome = {self._nome}'

class Tabela_Contato:
    id_counter = 0

    def __init__(self, cpf, telefone):
        self._id = Tabela_Contato.id_counter
        Tabela_Contato.id_counter += 1  
        self._cpf = cpf
        self._telefone = telefone

    def __str__(self):
        return f'ID = {self._id} | CPF = {self._cpf} | Telefone = {self._telefone}'

def main():
    print("-TABELA DE CONTATOS-")
    pessoa_nome = input("Qual o seu nome: ")
    pessoa_cpf = input("CPF: ")

    pessoa = Pessoa(pessoa_cpf, pessoa_nome)
    print(pessoa) 

    contatos = []

    while True:
        adicionar_contato = input("Você deseja adicionar um contato? (s/n): ").strip().lower()
        if adicionar_contato == 'n':
            break

        telefone = input("Digite o telefone do contato: ")
        contato = Tabela_Contato(pessoa_cpf, telefone)
        contatos.append(contato)
        print(f'Contato adicionado: {contato}')
    
    print("\nLista de contatos associados ao CPF", pessoa_cpf)
    for contato in contatos:
        print(contato)

main()