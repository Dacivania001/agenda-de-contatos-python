from contatos import Contatos
from pessoa import Pessoa
from endereco import Endereco
  

def listarPorLista(lista_de_contatos):
    
    if len(lista_de_contatos) == 0:
        print("=======================")
        print("A lista está vazia!    ")
        print("=======================")

    else:    
        for x in lista_de_contatos:

            print("========================================================")
            print("---------------- Informações listadas ------------------")
            print("<======================================================>")
            print(f"Nome completo: {x.pessoa.nome} {x.pessoa.sobrenome}")
            print(f"Apelido: {x.pessoa.apelido}")
            print(f"Numero do Contato: {x.numero_celular}")
            print(f"Nome do país: {x.pessoa.endereco.pais}")
            print(f"Nome do estado: {x.pessoa.endereco.estado}")
            print(f"Nome da cidade: {x.pessoa.endereco.cidade}")
            print(f"Nome da rua: {x.pessoa.endereco.rua}")
            print(f"Número da casa: {x.pessoa.endereco.numero}")
            print(f"Bairro: {x.pessoa.endereco.bairro}")
            print(f"Número do CEP: {x.pessoa.endereco.cep}")
            print("<======================================================>")