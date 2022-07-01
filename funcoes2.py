from gettext import find
from contatos import Contatos
from pessoa import Pessoa
from endereco import Endereco

def existeNome(lista_de_contatos,busca):
    for x in lista_de_contatos:
        if x.pessoa.nome.startswith(busca) == True:
            return x 

def seExistenumero(lista_de_contatos,busca):
    for x in lista_de_contatos:
        if x.pessoa.nome.startswith(busca) == True:
            return x         
    
def buscarContato(lista_de_contatos,busca):
    
    for x in lista_de_contatos:
        if x.pessoa.nome.startswith(busca) == True:
            print("====================================================")
            print("------------------ Nome encontrado -----------------")
            print("====================================================")
            print(f"Nome: {x.pessoa.nome}")
            print("====================================================")
            
            print("=====================================================")
            print("------------- Informações do contato ----------------")
            print("=====================================================")
            print(f"Nome completo: {x.pessoa.nome} {x.pessoa.sobrenome} ")
            print(f"Apelido: {x.pessoa.apelido}")
            print(f"Numero do Contato: {x.numero_celular}")
            print(f"Nome do país: {x.pessoa.endereco.pais}")
            print(f"Nome do estado: {x.pessoa.endereco.estado}")
            print(f"Nome da cidade: {x.pessoa.endereco.cidade}")
            print(f"Nome da rua: {x.pessoa.endereco.rua}")
            print(f"Número da casa: {x.pessoa.endereco.numero}")
            print(f"Bairro: {x.pessoa.endereco.bairro}")
            print(f"Número do CEP: {x.pessoa.endereco.cep}")
            print("=====================================================")
          
        
def buscarNumero(lista_de_contatos,busca):
    
    for x in lista_de_contatos:
        
        if x.numero_celular.startswith(busca) == True:
            
            print("====================================================")
            print("----------------- Número encontrado ----------------")
            print("====================================================")
            print(f"Nome: {x.numero_celular}")
            print("====================================================")
            
            print("=====================================================")
            print("------------- Informações do contato ----------------")
            print("=====================================================")
            print(f"Nome: {x.pessoa.nome}")
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
            print("=====================================================")
        
    
   
    
def buscarNomeOuNumero(lista_de_contatos):
    busca = input("Digite um nome ou número para procurar: \n").title()
    
    v1 = busca.replace(" ","").isalpha()
    v2 = busca.isdigit()
    
    
    if v1 == True:
        v01 = existeNome(lista_de_contatos,busca)
        
        if v01 == None:
            print("======================")
            print("Nome  não encontrado! ")
            print("======================")
            
        else:    
            buscarContato(lista_de_contatos,busca)
    
        
    elif v2 == True :
        v02 = seExistenumero(lista_de_contatos,busca)
        
        if v02 == None:
            print("======================")
            print("Número não encontrado!")
            print("======================")
        
        else:    
            buscarNumero(lista_de_contatos,busca)
        

          
    
    
        
    
           

        