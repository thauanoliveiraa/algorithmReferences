""" 
>> DE LIVRO ?
> SIM : 
+NUMERO DE AUTORES :
1 - INSERIR : Sobrenome, Nome, Título, Tem subtitulo ? (Sim : colocar / Não : Pass), Tem edição? (Sim : colocar / Não: Pass, Local de publicação, Editora, Data de publicação da obra Edição

<=3 - INSERIR : Quantos autores ? (máximo 3)
Loop até a quantidade de autores - INSERIR : 
Sobrenome, Nome,Título, Tem subtitulo ? (Sim : colocar / Não : Pass), Tem edição? (Sim : colocar / Não: Pass, Local de publicação, Editora, Data de publicação da obra

>3 - INSERIR : Quantos autores ? Colocar dados de todos ? (Sim : Gerar inputs até a quantidade de autores / Não : Gerar input de 1 autor e colocar et al)
INSERIR : Título, Tem subtitulo ? (Sim : colocar / Não : Pass), Tem edição? (Sim : colocar / Não: Pass, Local de publicação, Editora, Data de publicação da obra

== 0 - INSERIR : Título, Cidade, Editora, Ano de publicação, Página
> NÃO : PASS
"""

"""
VARIAVEIS :
referenceData = tipo de referencia (livro, ...)

"""
import os
from time import sleep
from weakref import ref
clear = lambda: os.system('cls')
referenceData = True

def verySmallTime():
    sleep(1)

def smallTime():
    sleep(2)

def biggestTime():
    sleep(4)    

def poweredBy():
    author = "-- REFERENCE FORMAT AND CREATOR SCRIPT -- \nPowered by Thauan Oliveira ©\nInstagram : @thx0liver \nGithub : https://github.com/thauanoliveiraa\nLinkedin : https://www.linkedin.com/in/thauan-de-oliveira-ramos-396b66224/\n"
    print(author)

term_of_use = True
while term_of_use:
    poweredBy()
    term_of_use = input("\nDo you agree to use and agree to all terms imposed by the author ?\n\n Say 'Y' (Yes) or 'N' (No) : ").upper()
    if term_of_use.isalpha() and term_of_use == 'Y':
        while referenceData:
            clear()
            smallTime()
            referenceData = input("-- TIPOS DE REFERENCIA --\n1 - LIVRO\n2 - ARTIGO ONLINE\n3 - ARTIGO DE REVISTA\n4 - CONSTITUIÇÃO FEDERAL OU ESTADUAL\n5 - LEGISLAÇÃO COMUM\n6 - TESE\n7 - SAIR\nPowered by : \nInsira o tipo de referencia a ser criada : ")
            if referenceData.isnumeric():
                referenceData = (int(referenceData)) 
                if referenceData == 1:
                    clear()
                    print("REFERÊNCIA PARA LIVRO")
                    authorQuantity = True
                    while authorQuantity:
                        authorQuantity = input("Insira a quantidade de autores : ")
                        if authorQuantity.isnumeric():
                            authorQuantity = (int(authorQuantity))
                            if authorQuantity == 0:
                                #== 0 - INSERIR : Título, Cidade, Editora, Ano de publicação, Página
                                Title = print("TESTE")
                                city = 
                                publishingCompany = 
                                publishingYear = 
                                page = 
                            elif authorQuantity == 1:
                                print("TESTE")    
                            elif authorQuantity <= 3:
                                print("TESTE")  
                            elif authorQuantity > 3:
                                print("TESTE")                                                       
                        else:
                            clear()
                            print("O que foi digitado não é um número, tente novamente")
                            smallTime()
                            authorQuantity = True                   
                    biggestTime()
                elif referenceData == 2:
                    clear()
                    print("REFERÊNCIA PARA ARTIGO ONLINE")
                    biggestTime()
                elif referenceData == 3:
                    clear()
                    print("REFERÊNCIA PARA ARTIGO DE REVISTA")
                    biggestTime()
                elif referenceData == 4:
                    clear()
                    print("REFERÊNCIA PARA CONSTITUIÇÃO CONSTITUIÇÃO FEDERAL OU ESTADUAL")
                    biggestTime()
                elif referenceData == 5:
                    clear()
                    print("REFERÊNCIA PARA LEGISLAÇÃO COMUM")  
                    biggestTime()
                elif referenceData == 6:
                    clear()
                    print("REFERÊNCIA PARA TESE")
                    biggestTime()
                elif referenceData == 7:        
                    clear()
                    print("SAINDO")
                    verySmallTime()
                    break            
                else:
                    clear()
                    print("Insira uma numeração válida")
                    smallTime()
                    continue 
            else:
                clear()
                print("O que foi digitado não é um número, tente novamente")
                smallTime()
                referenceData = True     

    elif term_of_use == 'N':
        clear()
        print("Exiting")
        sleep(2)
        term_of_use = False

    elif term_of_use.isnumeric() or term_of_use.isdigit() or term_of_use == '':
        clear()
        print("Try again")
        sleep(2)
        term_of_use = True
        #poweredByCls()   
    else:
        print
#else:
 #   print("Insira uma numeracao de ")
