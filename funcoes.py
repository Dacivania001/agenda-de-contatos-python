from contatos import Contatos
from pessoa import Pessoa
from endereco import Endereco

def veriExistInd(numero_celular):
    if len(numero_celular) == 12:
        return True
    else:
        return False

def seExisteNome(lista_de_contatos,nome):
    for x in lista_de_contatos:
        if nome == x.pessoa.nome:
            return x 

def seExisteNumero(lista_de_contatos,numero_celular):
    for x in lista_de_contatos:
        if numero_celular == x.numero_celular:
            return x 
        
def cadastroDeContato(lista_de_contatos):
    
    nome = str(input("Digite um nome: \n " )).title()
    v1 = nome.replace(" ","").isalpha()
    
        
    veri1 = seExisteNome(lista_de_contatos,nome)
    while v1 == False or veri1 != None:
        print("==============")
        print("ERRO NO NOME!")
        print("==============")
        
        nome = str(input("Digite um nome: \n " )).title()
        v1 = nome.replace(" ","").isalpha()
        veri1 = seExisteNome(lista_de_contatos,nome)
    if v1 == True and veri1 == None:
            
        sobrenome = str(input("Digite o sobrenome: \n ")).title()
        v2 = sobrenome.replace(" ","").isalpha()
        
        while v2 == False:
            print("====================")
            print("ERRO NO SOBRENOME!  ")
            print("====================")
            
            sobrenome = str(input("Digite o sobrenome: \n ")).title()
            v2 = sobrenome.replace(" ","").isalpha()
        if v2 == True : 
                
            apelido = str(input("Digite um apelido da pessoa: \n ")).title()
            v3 = apelido.replace(" ","").isalpha()
            while v3 == False:
                print("==================")
                print("ERRO NO APELIDO!  ")
                print("==================")
                
                apelido = str(input("Digite um apelido da pessoa: \n ")).title()
                v3 = apelido.replace(" ","").isalpha()
            if v3 == True : 
                    
                numero_celular = input("Digite o número de contato com DDD: \n ")
                    
                v4 = numero_celular.isdigit()
                ind = veriExistInd(numero_celular)
                veri2 = seExisteNumero(lista_de_contatos,numero_celular)
                while v4 == False or ind == False or veri2 != None :
                    print("============================")
                    print("ERRO NO NÚMERO DE CELULAR! ")
                    print("============================")
                    
                    numero_celular = input("Digite o número de contato com DDD: \n ")
                    v4 = numero_celular.isdigit()
                    veri2 = seExisteNumero(lista_de_contatos,numero_celular)
                if v4 == True and ind == True and veri2 == None :
                        
                    pais = str(input("Qual é o nome do país que reside? \n ")).title()
                    v5 = pais.replace(" ","").isalpha()
                    while v5 == False :
                        print("=======================")
                        print("ERRO NO NOME DE PAÍS ! ") 
                        print("=======================")
                        
                        pais = str(input("Qual é o nome do país que reside? \n ")).title()
                        v5 = pais.replace(" ","").isalpha()
                    if v5 == True : 
                            
                        
                        estado = str(input("Qual é o nome do Estado que reside? \n ")).title()
                        v6= estado.replace(" ","").isalpha()
                        while v6 == False :
                            print("=========================")
                            print("ERRO NO NOME DO ESTADO ! ") 
                            print("=========================")
                            
                            estado = str(input("Qual é o nome do Estado que reside? \n ")).title()
                            v6= estado.replace(" ","").isalpha()
                        if v6 == True : 
                                
                            cidade = str(input("Qual é o nome da cidade que reside? \n ")).title()
                            v7 = cidade.replace(" ","").isalpha()
                            while v7 == False :
                                print("============================") 
                                print("ERRO NO NO NOME DA CIDADE ! ")
                                print("============================")
                                
                                cidade = str(input("Qual é o nome da cidade que reside? \n ")).title()
                                v7 = cidade.replace(" ","").isalpha()
                            if v7 == True :
                                    
                                rua = str(input("Qual é o nome da rua que reside? \n ")).title()
                                v8 = rua.replace(" ","").isalpha()
                                while v8 == False :
                                    print("=====================")
                                    print("ERRO NO NOME DA RUA! ")
                                    print("=====================")
                                    
                                    rua = str(input("Qual é o nome da rua que reside? \n ")).title()
                                    v8 = rua.replace(" ","").isalpha()
                                if v8  == True :
                                        
                                    numero_casa = input("Qual é o número da casa? \n ")
                                    v9 = numero_casa.isdigit()
                                    while v9 == False:
                                        print("=========================")
                                        print("ERRO NO NÚMERO DA CASA ! ")
                                        print("=========================")
                                        
                                        numero_casa = input("Qual é o número da casa? \n ")
                                        v9 = numero_casa.isdigit()
                                            
                                    if v9 == True :
                                            
                                        bairro = str(input("Qual é o nome do bairro? \n ")).title()
                                        v10 = bairro.replace(" ","").isalpha()
                                        while v10 == False :
                                            print("=================")
                                            print("ERRO NO BAIRRO ! ")
                                            print("=================")
                                            
                                            bairro = str(input("Qual é o nome do bairro? \n ")).title()
                                            v10 = bairro.replace(" ","").isalpha()
                                        if v10  == True :
                                            
                                            cep = input("Qual é o número do CEP? \n ")
                                            v11 = cep.isdigit()
                                            
                                            while v11 == False or len(cep) != 8 :
                                                print("==============")
                                                print("ERRO NO CEP! ")
                                                print("==============")
                                                
                                                print("======================================")
                                                print("Lembre-se, que todo CEP tem 8 digitos!")
                                                print("======================================")
                                                
                                                cep = input("Qual é o número do CEP? \n ")
                                                v11 = cep.isdigit()
                                                
                                            if v11 == True and len(cep) == 8:
                                                
                                                                    
                                                arquivo01 = open("informacoesdoscontatos.txt","a")
                                                
                                                obj_endereco = Endereco(pais,estado,cidade,rua,numero_casa,bairro,cep)
                                                obj_pessoa = Pessoa(nome,sobrenome,apelido,obj_endereco)
                                                obj_contato = Contatos(numero_celular,obj_pessoa)
                                                lista_de_contatos.append(obj_contato)
                                                
                                                arquivo01.write(f"{nome}-{sobrenome}-{apelido}-{numero_celular}-{pais}-{estado}-{cidade}-{rua}-{numero_casa}-{bairro}-{cep}\n")
                                                arquivo01.close()
       
            