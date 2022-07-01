
from contatos import Contatos
from pessoa import Pessoa
from endereco import Endereco
import funcoes,funcoes2,funcoes3,funcoes4,funcoes5,arquivo,menu



lista_de_contatos = []

while True:
    menu.menuPrimario()
    opcao = input("Escolha uma opção do menu: \n")

    if opcao == "1":
        print(" Cadastar um novo contato... ")
        funcoes.cadastroDeContato(lista_de_contatos)
        
        print("===========================")
        print("Contato salvo com sucesso!")
        print("===========================")
    
    elif opcao == "2" :
        print("Procurando um contato ...")
        funcoes2.buscarNomeOuNumero(lista_de_contatos)
        
        
    elif opcao == "3" :
        print("Alterando um contato... ")
        buscanome = input("Digit um nome: \n").title()
        
        veri = funcoes3.encontrarNome(lista_de_contatos,buscanome)
        
        if veri == None:
            print("Nome não encontrado")
            
        else:
            
            while True:
                
                
                menu.quartoMenu()
                opcc = input("Digite uma das opções acima: \n")
                
                if opcc == "1":
                    print("Alterando nome...")
                    funcoes3.alterarNome(lista_de_contatos,veri)
                        
                elif opcc == "2":
                    print("Alterando sobrenome...")
                    funcoes3.alterarSobrenome(veri)
                    
                elif opcc == "3":
                    print("Alterando apelido...")
                    funcoes3.alterarApelido(veri)
                    
                       
                elif opcc == "4":
                    print("Alterando o número do celular...")
                    funcoes3.alterarNumeroCelular(lista_de_contatos,veri)
        
                elif opcc == "5":
                    print("Alterando o nome do país...")
                    funcoes3.alterarPais(veri)
                    
                
                elif opcc == "6":
                    print("Alterando o nome do estado...")
                    funcoes3.alterarEstado(veri)
                    
                elif opcc == "7":
                    print("Alterando o nome da cidade...")
                    funcoes3.alterarCidade(veri)
                    
                
                elif opcc == "8":
                    print("Alterando o nome da rua...")
                    funcoes3.alterarNomeRua(veri)
                    
                elif opcc == "9":
                    print("Alterando o número da casa...")
                    funcoes3.alterarNumeroCasa(veri)
                    
                elif opcc == "10":
                    print("Alterando o bairro...")
                    funcoes3.alterarBairro(veri)
                    
                
                elif opcc == "11":
                    print("Alterando o CEP...")
                    funcoes3.alterarCep(veri)
        
                    
                elif opcc == "12":
                    print("Saindo...")
                    break
        
                else:
                    print("-------------------------------------------")
                    print("Opção inválida!")
                    print("-------------------------------------------")
                    print("Digite novamente uma opção!")
                    print("-------------------------------------------")


    elif opcao == "4" :
        print("Excluindo um contato... ")
        
        while True:
            menu.menuTerciario()
            op = input("Digite uma das opções acima: \n")

            if op == "1":
                funcoes4.deletecontato(lista_de_contatos)

            elif op == "2":
                print("Deletando todo o arquivo...")
                funcoes4.deletarNoArquivo()

            elif op == "3":
                print("Saindo...")
                break
    
            else:
                print("-------------------------------------------")
                print("Opção inválida!")
                print("-------------------------------------------")
                print("Digite novamente uma opção!")
                print("-------------------------------------------")


        
    elif opcao == "5":
        print("Listando todos contatos...")
        
        while True:
            menu.menuSegundario()
        
            opc = input("Escolha uma opção: ")
            
            if opc == "1":
                print("Listando todos contatos...")
                
                funcoes5.listarPorLista(lista_de_contatos)
                
            elif opc == "2":
                print("Listando todos contatos por arquivo")
                
                arquivo.arquivo1(lista_de_contatos)
                
            elif opc == "3":
                print("Saindo...")
                break
    
            else:
                print("-------------------------------------------")
                print("Opção inválida!")
                print("-------------------------------------------")
                print("Digite novamente uma opção!")
                print("-------------------------------------------")
                
        
    elif opcao == "6" :
        print("Saindo...")
        break
    
    else:
        print("-------------------------------------------")
        print("Opção inválida!")
        print("-------------------------------------------")
        print("Digite novamente uma opção!")
        print("-------------------------------------------")
