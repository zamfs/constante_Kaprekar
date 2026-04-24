numero = float(input())

#Validaçao de tipo
if (numero > 0) and (numero % 1 == 0):
    numero = int(numero) #Tranformando para inteiro, após verficar se o usuário digitou um float

    continuar = True

    #o programa tem que funcionar até o número ser igual a 6174
    while(numero != 6174 and continuar == True):

        #Validação de faixa
        if numero <= 9999:
            #Separar cada dígito
            digito1 = numero//1000
            digito2 = (numero//100)%10
            digito3 = (numero//10)%10
            digito4 = (numero%10)
           
            #criando as variáveis que irão guardar o numero crescente e o decrescente
            crescente = 0
            decrescente = 0

            #Validação de repetição de dígitos
            if (digito1 == digito2 == digito3) or (digito2 == digito3 == digito4) or (digito3 == digito4 == digito1) or (digito1 == digito2 == digito4):
                print('Número possui 3 ou 4 repetições!')
                continuar = False
           
            #se não tiver mais de 3 números repetidos, vai para o restante do código
            else:

                #declarando variaveis que serão utilizadas depois
                teste1, teste2, teste3 = 0, 0, 0
                maior, segundo_maior, segundo_menor, menor = 0, 0, 0, 0

                #primeiro descobrir o maior digito
                #guarda o restante em outras var para não precisar fazer muitos outros if elif e else
                if (digito1 >= digito2) and (digito1 >= digito3) and (digito1 >= digito4):
                    maior = digito1

                    teste1 = digito2
                    teste2 = digito3
                    teste3 = digito4

                elif (digito2 >= digito1) and (digito2 >= digito3) and (digito2 >= digito4):
                    maior = digito2

                    teste1 = digito1
                    teste2 = digito3
                    teste3 = digito4

                elif (digito3 >= digito1) and (digito3 >= digito2) and (digito3 >= digito4):
                    maior = digito3

                    teste1 = digito1
                    teste2 = digito2
                    teste3 = digito4

                elif (digito4 >= digito1) and (digito4 >= digito2) and (digito4 >= digito3):
                    maior = digito4

                    teste1 = digito1
                    teste2 = digito2
                    teste3 = digito3
               
                #comparando os numeros restantes
                if (teste1 >= teste2) and (teste1 >= teste3):
                    segundo_maior = teste1
                    if teste2 >= teste3:
                        segundo_menor = teste2
                        menor = teste3
                    else:
                        segundo_menor = teste3
                        menor = teste2
                elif teste2 >= teste3:
                    segundo_maior = teste2
                    if teste1 >= teste3:
                        segundo_menor = teste1
                        menor = teste3
                    else:
                        segundo_menor = teste3
                        menor = teste1
                else:
                    segundo_maior = teste3
                    if teste1 >= teste2:
                        segundo_menor = teste1
                        menor = teste2
                    else:
                        segundo_menor = teste2
                        menor = teste1

                #colocando os numeros em ordem nas variáveis
                crescente = menor*1000 + segundo_menor*100 + segundo_maior*10 + maior
                decrescente = maior*1000 + segundo_maior*100 + segundo_menor*10 + menor

                #fazendo a subtração do maior pelo menor
                numero = decrescente - crescente

                #montando a mensagem que aparecerá para o usuário
                print(f'{decrescente} - {crescente} = {numero}')

        else:
            print('Número possui mais de 4 números')
            continuar = False

else:
    print('Número não é positivo ou não é inteiro.')