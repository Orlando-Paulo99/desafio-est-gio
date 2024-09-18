''' 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser 
previamente definido no código; '''

"variavel que vai receber para verificar se está na seuqencia   "
novo_num=int(input("DIGITE UM NUMERO"))

" variavel em que fica amazenado os números da sequencia "
sequencia=[ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

" um loop que vai somar os dois ultimos números  da sequencia"
for x in range(2,novo_num):
    "calculando o uktmi e o penultimo numero"
    prox=sequencia[-1] + sequencia[-2]

    "verificando se o numero calculado é maior que ummero digitado e adicionando a lista"
    if prox > novo_num:
        break
    sequencia.append(prox)

"codiçaõ que verifica se o numero digitado pertence a lista "
if novo_num in sequencia:
    print("o numero está na sequencia",sequencia)

else:
    print("não está na seuqencia ")