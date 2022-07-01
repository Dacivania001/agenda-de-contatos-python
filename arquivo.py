from contatos import Contatos
from pessoa import Pessoa
from endereco import Endereco

def arquivo1(lista_de_contatos):
    
    arquivo = open("informacoesdoscontatos.txt","r")
    
    
    lista_de_contatos = arquivo.readlines()
    
    
    for listar in lista_de_contatos:
        
        print("==========================================================")
        print(f"Informações do contato:{listar[0:-1]}")
        print("==========================================================")
    
      
    arquivo.close()