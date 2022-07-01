from contatos import Contatos
from pessoa import Pessoa
from endereco import Endereco
import funcoes

def deletecontato(lista_de_contatos):
    nome = input("digite nome: ").title()
    seexistenome = funcoes.seExisteNome(lista_de_contatos,nome)
    
    if seexistenome == None:
        print("=====================")
        print("Nome não encontrado! ")
        print("=====================")
        
        
    else:
        lista_de_contatos.remove(seexistenome)
        print("=======================")
        print("O contato foi excluido!")
        print("=======================")
        

def deletarNoArquivo():
    #deleta tudo que esta em arquivo, ou seja, limpa o arquivo.
    
    with open("informacoesdoscontatos.txt", 'r+') as f:
        f.truncate(0)
        
        print("==============================")
        print("O arquivo foi todo excluindo! ")
        print("==============================")

	
    
    