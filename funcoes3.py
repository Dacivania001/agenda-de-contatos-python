
from contatos import Contatos
from pessoa import Pessoa
from endereco import Endereco

def encontrarNome(lista_de_contatos,buscanome):
    
    for x in lista_de_contatos:
        if x.pessoa.nome == buscanome:
            return x

def encontrarNumero(lista_de_contatos,buscarnumero):
    for x in lista_de_contatos:
        if buscarnumero == x.numero_celular:
            return x
        
def alterarNome(lista_de_contatos,veri):
    buscanome = input("Digite o novo nome: \n").title()
    m1 = buscanome.replace(" ","").isalpha()
    k1 = encontrarNome(lista_de_contatos,buscanome)
    while m1 == False or k1 != None:
        print("ERRO! Na digitação")
        buscanome = input("Digite o novo nome: \n").title()
        m1 = buscanome.replace(" ","").isalpha()
        k1 = encontrarNome(lista_de_contatos,buscanome)               
    else:
        veri.pessoa.nome = buscanome
        
        print("====================")
        print("Alteração concluída!")
        print("====================")
        
def alterarSobrenome(veri):
    buscanome = input("Digite o novo sobrenome: \n").title()
    m1 = buscanome.replace(" ","").isalpha()
    while m1 == False :
        print("ERRO! Na digitação")
        buscanome = input("Digite o novo sobrenome: \n").title()
        m1 = buscanome.replace(" ","").isalpha()
                        
    else:
        veri.pessoa.sobrenome = buscanome
        
        print("====================")
        print("Alteração concluída!")
        print("====================")


def alterarApelido(veri):
    buscanome = input("Digite o novo Apelido: \n").title()
    m1 = buscanome.replace(" ","").isalpha()
                        
    while m1 == False :
        print("ERRO! Na digitação")
        buscanome = input("Digite o novo Apelido: \n").title()
        m1 = buscanome.replace(" ","").isalpha()
                        
    else:
        veri.pessoa.apelido = buscanome
        
        print("====================")
        print("Alteração concluída!")
        print("====================")
        

def alterarNumeroCelular(lista_de_contatos,veri):
    buscarnumero = input("Digite o novo número: \n")
    ve1 = buscarnumero.isdigit()
    
    zx = encontrarNumero(lista_de_contatos,buscarnumero)
    
    while ve1 == False or zx != None  or len(buscarnumero)!= 12:
        print("=====")
        print("Erro!")
        print("=====")
        
        buscarnumero = input("Digite um novo número: \n")
        ve1 = buscarnumero.isdigit()
    
        zx = encontrarNumero(lista_de_contatos,buscarnumero)
        
    else:
        veri.numero_celular = buscarnumero
        
        print("====================")
        print("Alteração concluída!")
        print("====================")
        
        
def alterarPais(veri):
    buscanome = input("Digite novo nome para o país: \n").title()
    m1 = buscanome.replace(" ","").isalpha()
    while m1 == False :
        print("ERRO! Na digitação!")
        buscanome = input("Digite novo nome para o país: \n").title()
        m1 = buscanome.replace(" ","").isalpha()
                        
    else:
        veri.pessoa.endereco.pais = buscanome
        
        print("====================")
        print("Alteração concluída!")
        print("====================")
        

def alterarEstado(veri):
    buscanome = input("Digite um novo nome para o estado: \n").title()
    m1 = buscanome.replace(" ","").isalpha()
    while m1 == False :
        print("ERRO! Na digitação!")
        buscanome = input("Digite um novo nome para o estado: \n").title()
        m1 = buscanome.replace(" ","").isalpha()
                        
    else:
        veri.pessoa.endereco.estado = buscanome
        
        print("====================")
        print("Alteração concluída!")
        print("====================")
        

def alterarCidade(veri):
    buscanome = input("Digite um novo nome para a cidade: \n").title()
    m1 = buscanome.replace(" ","").isalpha()
                        
    while m1 == False :
        print("ERRO! Na digitação")
        buscanome = input("Digite um novo nome para a cidade: \n").title()
        m1 = buscanome.replace(" ","").isalpha()
                        
    else:
        veri.pessoa.endereco.cidade = buscanome
        
        print("====================")
        print("Alteração concluída!")
        print("====================")

def alterarNomeRua(veri):
    buscanome = input("Digite um novo nome para a rua: \n").title()
    m1 = buscanome.replace(" ","").isalpha()
    while m1 == False :
        print("ERRO! Na digitação")
        buscanome = input("Digite um novo nome para a rua: \n").title()
        m1 = buscanome.replace(" ","").isalpha()
                        
    else:
        veri.pessoa.endereco.rua = buscanome
        
        print("====================")
        print("Alteração concluída!")
        print("====================")
        

def alterarNumeroCasa(veri):
    buscarnumero = input("Digite o novo número: \n")
    ve1 = buscarnumero.isdigit()
    while ve1 == False :
        print("=====")
        print("Erro!")
        print("=====")
        
        buscarnumero = input("Digite o novo número: \n")
        ve1 = buscarnumero.isdigit()
        
    else:
        veri.pessoa.endereco.numero_casa = buscarnumero
        
        print("====================")
        print("Alteração concluída!")
        print("====================")
           
           
def alterarBairro(veri):
    print("ERRO! Na digitação")
    buscanome = input("Digite um novo nome para o bairro: \n").title()
    m1 = buscanome.replace(" ","").isalpha()
    while m1 == False :
        print("ERRO! Na digitação")
        buscanome = input("Digite um novo nome para o bairro: \n").title()
        m1 = buscanome.replace(" ","").isalpha()
                        
    else:
        veri.pessoa.endereco.bairro = buscanome
        
        print("====================")
        print("Alteração concluída!")
        print("====================")
        
def alterarCep(veri):
    buscarnumero = input("Digite o novo CEP: \n")
    ve1 = buscarnumero.isdigit()
    while ve1 == False or len(buscarnumero) != 8 :
        print("=====")
        print("Erro!")
        print("=====")
        
        buscarnumero = input("Digite o novo CEP: \n")
        ve1 = buscarnumero.isdigit()
        
    else:
        veri.pessoa.endereco.cep = buscarnumero
        
        print("====================")
        print("Alteração concluída!")
        print("====================")
           


