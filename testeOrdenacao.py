# PROBABILIDADE E ESTATÍSTICA --- CALCULO DA CURVA POLIDA

import math
#lista = [15,18,18,16,15,23,18,19,23,19,18,15,19,16,19,17,15,19,19,22,18,16,19,21,18,18,20,16,34,21,23,17,20,20]
lista = [150, 155, 160, 162, 166, 151, 156, 160, 162, 167, 152, 156, 160, 163, 168, 153, 156, 160, 163, 168, 154, 157, 161, 164, 169, 155, 158, 161, 164, 170, 155, 158, 161, 164, 172, 155, 160, 161, 165, 173]
#lista = [17,18,16,24,23,42,40,36,15,18,26,23,23,24,28,41,16,18,20,27]
tamanho_lista = len(lista)
nova_lista = list()
lista_repeticao = list()
lista_frequencia = list()
lista_teste = list()
curva_frequencia = list()

print("PROBABILIDADE E ESTATÍSTICA --- CURVA POLIDA")
print("\nLista inserida: ")
print(lista)
print(" ")

# FUNÇÃO SORT PARA ORGANIZAR A LISTA EM ORDEM CRESCENTE.
lista.sort()
print("Lista ordenada: ")
print(lista)
print(" ")


# CONTAGEM DE OCORRENCIAS DE UM DETERMINADO VALOR E EXCLUSÃO DE OCORRENCIAS REPETIDAS.
for c in lista:
    if c not in nova_lista:
        repeticoes = lista.count(c)
        nova_lista.append(c)
        lista_repeticao.append(repeticoes)

lista_teste = nova_lista.copy()
lista_teste1 = nova_lista.copy()


# APRESENTAR LISTA SEM VALORES REPETIDOS E MOSTRAR QUANTAS OCORRENCIAS TIVERAM.
for c in range(len(nova_lista)):
    print("O numero", nova_lista[c], "se repete: ", lista_repeticao[c]," vez(es)")

# FREQUENCIA DE CLASSES.
frequencia_classes = round(1+(3.3 * math.log10(len(lista))))
print("\nFrequencia de classes: ", frequencia_classes)


#AMPLITUDE AMOSTRAL.
amplitude_amostral = math.ceil((nova_lista[-1] - nova_lista[0]) / frequencia_classes)
print("\nAmplitude amostral: ", amplitude_amostral)
print(" ")

# SOMA E ARMAZENAMENTO DA QUANTIDADE DE OCORRENCIAS DE UM DETERMINADO VALOR.
lista_teste2 = lista_repeticao.copy()

cont = 0
soma = 0
flag_valor = lista[0]
flag_index = flag_valor + amplitude_amostral

while True:
    if(flag_index > lista[-1]):
        lista_frequencia.append(len(lista))
        break
    elif(lista[cont] < flag_index):
        soma = soma + 1
        cont = cont + 1
    else:
        lista_frequencia.append(soma)
        del(lista[0:cont])
        cont = 0
        soma = 0
        flag_index = flag_index + amplitude_amostral
        

# CALCULO DA CURVA POLIDA. 
for c in range(len(lista_frequencia)):
    if lista_frequencia[c] == lista_frequencia[0] and c == 0:
        cp = (0+(2*lista_frequencia[0])+ lista_frequencia[1])/4

    elif lista_frequencia[c] == lista_frequencia[-1] and c != 0:
        cp = (lista_frequencia[-2]+(2*lista_frequencia[-1])+ 0)/4

    else:
        cp =(lista_frequencia[c - 1]+(2*lista_frequencia[c])+ lista_frequencia[c + 1])/4

    curva_frequencia.append(cp)
    

#PRINT DO RESULTADO 
cont = 0

for nova_lista in range(nova_lista[0],nova_lista[-1],amplitude_amostral):
    print("|", nova_lista, "|-----  ", nova_lista + amplitude_amostral, "| ", lista_frequencia[cont], " --> ", curva_frequencia[cont])
    cont = cont + 1










      
    

