import math
#-------Utilizando Python 3
'''1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.'''
#print("Alo mundo")
'''2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]'''
#numero = input("Digite um numero ");
#print("O número digitado foi:"+numero);
'''3 - Faça um Programa que peça dois números e imprima a soma.'''
#num1 = int(input('Entre com o 1º valor: '))
#num2 = int(input('Entre com o 2º valor: '))
#soma = num1 + num2
#print ('A soma eh: ',soma)
'''4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média'''
#nota_1 = float(input('Nota 1: '))
#nota_2 = float(input('Nota 2: '))
#nota_3 = float(input('Nota 3: '))
#nota_4 = float(input('Nota 4: '))
#soma = float (nota_1+nota_2+nota_3+nota_4) 
#media = soma / 4;
#print('Média final eh: '+ format(media))
'''5 - Faça um Programa que converta metros para centímetros.'''
#metros = float (input('Digite a quantidade de metros que deseja converter para cm: '))
#cm = metros *100
#print('Centimetros' , cm)
'''6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''
#raio = float(input('Raio: '))
#area = math.pi * (raio**2)
#print("Área: ",area)
'''7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.'''
#lado = float(input('Lado: '))
#area = (lado**2)
#print('Area :',area)
#area = area * 2
#print('Dobro da area: ',area)
'''8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''
#dinheiro = float(input('Quanto você ganha por hora? '))
#hora = float(input('Quantas horas você trabalhou no mês? '))
#salario = hora * dinheiro
#print('Salário final :'+format(salario))
'''9  -Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).'''
#farenheit = float(input('Farenheit :'))
#c = (5*(farenheit -32) / 9)
#print('Celsius: ', c)
'''10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.'''
#c = float(input('Celsius :')) 
#f = (c * 9/5) + 32
#print('Farenheit: ', f)
'''11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''
#n1 = int(input('Digite o primeiro numero:  '))
#n2 = input('Digite o segundo numero:  ')
#nReal = float(input('Digite o numero Real:  '))
#r1 = n1 * 2 * (n2 / 2)          
#print ('O produto do dobro do primeiro com metade do segundo = ', format(r1))   
#r2 = n1 *  3 + nReal
#print ('a soma do triplo do primeiro com o terceiro = ', format(r2))
#r3 = nReal ** 3
#print ('o terceiro elevado ao cubo', format(r3))
'''12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''
#a = float(input('Altura: '));
#ideal = (72.7*a) - 58
#print('Peso ideal: ', format(ideal))
'''13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''
#s = input('Digite m para masculino e f para feminino: ')
#if s in 'f':
#    h = float(input('Altura: '))
#    ideal = (62.1*h) - 44.7
#    print('Altura ideal para mulheres: ',ideal);
#elif s in 'm':
#    h = float(input('Altura: '))
#    ideal = (72.7*h) -58
#    print('Altura ideal para homens: ',ideal)
'''14- João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João 
deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''
#peso = int(input("Entre com o peso: "))
#if peso > 50:
#	excesso = peso - 50
#	multa   = excesso * 4
#else:
#	excesso = "ZERO"
#	multa = "ZERO"
#print ('O excesso de peso foi de ',format(excesso),'kg, portanto, a multa é de R$', format(multa))
''' 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''
#qH =float(input("Quanto você ganha por hora: "))
#hT =float(input("Quantas horas você trabalhou: "))
#salarioB = qH * hT
#ir = (11/100.0 * salarioB)
#inss = (8/100.0 * salarioB)
#sindicato = (5/100.0 * salarioB)
#vT = ir + inss + sindicato
#salarioL = salarioB - vT
#print ('Seu salário bruto é',salarioB)
#print ('Valor dos impostos:')
#print ('IR: ',ir)
#print ('INSS: ',inss)
#print ('Sindicato: ',sindicato)
#print ('Seu salário liquido é: ',salarioL)
'''16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''
#tamanho = int(input('Tamanho em metros quadrados: '))
#litros = tamanho / 3
#if tamanho % 54 == 0:
#	latas = tamanho / 54
#else: 
#	latas = int(tamanho / 54) + 1
#preco = latas * 80

#print ('%d latas' %latas)
#print ('R$ %.2f' %preco)
'''17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''


'''18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''
#tamanho = float(input('Tamanho do arquivo (MB): '))
#velocidade = float(input('Velocidade de Internet (MBps): '))
#print('Tempo aproximado de download: %.0f Minutos ' %((tamanho / velocidade) * 60))

