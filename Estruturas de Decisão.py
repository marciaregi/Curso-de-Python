import math
'''1 - Faça um Programa que peça dois números e imprima o maior deles.'''
#n1 = int(input('Numero 1: '))
#n2 = int(input('Numero 2: '))
#if n1>n2:
#    print('Numero maior', n1)
#else:
#    print('Numero maior', n2)
'''2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''
#n1 = int(input('Digite o primero numero: '))
#if n1 < 0:
#    print ('O numero é negativo')
#else:
#    print ('O numero é positivo')
'''3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, 
Sexo Inválido.'''
#s = input('Sexo- F - Feminino, M - Masculino : ')
#if s in 'F, f':
#    print('Feminino')
#elif s in 'M, m':
#    print('Masculino')
#else:
#    print('Sexo Inválido')
'''4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''
#l = input('letra: ')
#if l in 'a, e, i, o, u , A, E, I , O, U':
#    print('Vogal')
#else:
#    print('Consoante')
'''5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.'''
#n1 = float(input('Nota 1: '))
#n2 = float(input('Nota 2: '))
#media = (n1+n2) / 2 
#if media >= 7.0 and media <= 9.9:
#    print('Aprovado')
#elif media < 6.9: 
#    print('Reprovado')
#elif media >= 10.0:
#    print('Aprovado com Distinção')
'''6 - Faça um Programa que leia três números e mostre o maior deles.'''
#n1 = int(input('Primeiro número: '))
#n2 = int(input('Segundo número: '))
#n3 = int(input('Terceiro número: '))
#maior = n1
#menor = n1
#if maior < n2:
#   maior = n2
#if maior < n3: 
#	maior = n3
#print ('Maior:  %d ' %maior)
'''7 - Faça um Programa que leia três números e mostre o maior e o menor deles.'''
#n1 = int(input('Primeiro número: '))
#n2 = int(input('Segundo número: '))
#n3 = int(input('Terceiro número: '))
#maior = n1
#menor = n1
#if maior < n2:
#    maior = n2
#if maior < n3: 
#	maior = n3
#if menor > n2:
#    menor = n2
#if menor > n3:
#	menor = n3
#print ('Maior:  %d ' %maior)
#print ('Menor:  %d ' %menor)
'''8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''
#p1 = float(input("Digite o 1° preço: "))
#p2 = float(input("Digite o 2° preço: "))
#p3 = float(input("Digite o 3° preço: "))
#if p1 < p2 and p1 < p3:
#    print ('O produto 1 é o mais barato!!')
#elif p2 < p1 and p3:
#    print ('O produto 2 é o mais barato!!')
#elif p3 < p1 and p2:
#    print ('O produto 3 é o mais barato!!')
#elif p1 == p2 and p1 and p2 < p3:
#    print ('O produto 1 e 2 são os mais baratos!!')
#elif p1 == p3 and p1 and p3 < p2:
#    print ('O produto 1 e 3 são os mais baratos!!')
#elif p2 == p3 and p2 and p3 < p1:
#    print ('O produto 1 e 2 são os mais baratos!!')
#else:
#    print ('Todos os preços são iguais!!')
'''9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.'''
#x=int(input("Entre com um numero: "))
#y=int(input("Entre com mais um numero: "))
#z=int(input("Entre com mais outro numero: "))
#if (x>y)&(x>z):
    #if y>z:
        #print (x)
        #print (y)
        #print (z)
    #else:
        #print (x)
        #print (y)
        #print (z)
#if (y>x)&(y>z):
    #if x>z:
        #print (y)
        #print (x)
        #print (z)
    #else:
        #print (y)
        #print (z)
        #print (x)
#if (z>x)&(z>y):
    #if x>y:
        #print (z)
        #print (x)
        #print (y)
    #else:
        #print (z)
        #print (y)
        #print (x)
#if (x==y)or(x==z)or(y==z):
    #print ("Existem dois numeros iguais!")
'''10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. '''      
#t = input('Qual turno voce estuda?  M-matutino ou V-Vespertino ou N- Noturno : ')
#if t in 'M, m':
#    print('Matutino')
#elif t in 'V, v':
#    print('Vespertino')
#elif t in 'N, n':
#    print('Noturno')
#else:
#    print('Sexo Inválido') 
'''11 - s Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento'''
#salario = float(input('Digite seu salário: '))
#if salario <= 280.00:
#    por = (20 / 100.0) * salario
#    resultado = salario + por
#    print ('Seu salário antes do reajuste: R$', salario)
#    print ('Percentual aumentado: %',20)
#    print ('O valor do aumento é: R$',por)
#    print ('Com o reajuste, o seu salário é: R$',resultado)
#elif salario > 280.00 and salario <= 700.00:
#    por = (15 / 100.0) * salario
#    resultado = salario + por
#    print ('Seu salário antes do reajuste: R$',salario)
#    print ('Percentual aumentado: %',15)
#    print ('O valor do aumento é: R$',por)
#    print ('Com o reajuste, o seu salário é: R$',resultado)
#elif salario > 700.00 and salario <= 1500.00:
#    por = (10 / 100.0) * salario
#    resultado = salario + por
#    print ('Seu salário antes do reajuste: R$',salario)
#    print ('Percentual aumentado: %',10)
#    print ('O valor do aumento é: R$',por)
#    print ('Com o reajuste, o seu salário é: R$',resultado)
#elif salario > 1500.00:
#    por = (5 / 100.0) * salario
#    resultado = salario + por
#    print ('Seu salário antes do reajuste: R$',salario)
#    print ('Percentual aumentado: %',5)
#    print ('O valor do aumento é: R$',por)
#    print ('Com o reajuste, o seu salário é: R$',resultado)
'''12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''
#horas = float(input('Digite o numero de horas trabalhadas: '))
#ganhos = float(input('Digite o ganho por horas: '))
#bruto = ganhos * horas
#cinco = (5 / 100.0) * bruto
#dez = (10 / 100.0) * bruto
#vinte = (20 / 100.0) * bruto
#onze = (11 / 100.0) * bruto
#if bruto <= 900:
#    print ('Seu salário bruo é de:',bruto, cinco)
#    print ('(-) IR (5%) :',' R$',cinco)
#    print ('(-) INSS ( 10%):','R$',dez)
#    print ('FGTS (11%): ',' R$',onze)
#    print ('Total de descontos:','R$',cinco + dez + onze)
#    print ('Salário Liquido :',' R$',bruto , (cinco + dez + onze) )
#elif bruto >= 900 and bruto <= 1500:
#    print ('Seu salário bruto é de:',bruto , dez)
#    print ('(-) IR (5%) :','R$',cinco)
#    print ('(-) INSS ( 10%):','R$',dez)
#    print ('FGTS (11%): ',' R$',onze)
#    print ('Total de descontos:','R$',cinco + dez + onze)
#elif bruto > 1500:
#    print ('Seu salário bruo é de:',bruto , vinte)
#    print ('(-) IR (5%) :',' R$',cinco)
#    print ('(-) INSS ( 10%):','R$',dez)
#    print ('FGTS (11%): ',' R$',onze)
#    print ('Total de descontos:','R$',cinco + dez + onze)
'''13 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''
#numero = int(input('Digite um numero: '))
#if numero == 1:
#    print ('1-Domingo')
#elif numero == 2:
#    print ('2-Segunda')
#elif numero == 3:
#    print ('3-Terça')
#elif numero == 4:
#    print ('4-Quarta')
#elif numero == 5:
#    print ('5-Quinta')
#elif numero == 6:
#    print ('6-Sexta')
#elif numero == 7:
#    print ('7-Sabádo')
#else:
#    print ('Entrada invalida')
'''14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
   algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''
#v1 = int(input('Digite o valor da primeira nota: '))
#v2 = int(input('Digite o valor da segunda nota: '))
#nota = (v1 + v2) /2
#if nota >= 9 and nota <= 10:
#    print ('A nota da primeira prova: ',v1)
#    print ('A nota da segunda prova: ',v2)
#    print ('——————————')
#    print ('Você tirou um A!')
#    print ('Sua media é de: ',nota)
#    print ('você foi aprovado!!')
#elif nota >= 7.5 and nota < 9:
#    print ('A nota da primeira prova: ',v1)
#    print ('A nota da segunda prova: ',v2)
#    print ('——————————')
#    print ('Você tirou um B!')
#    print ('Sua media é de: ',nota)
#    print ('você foi aprovado!!')
#elif nota >= 6.5 and nota < 7.5:
#    print ('A nota da primeira prova: ',v1)
#    print ('A nota da segunda prova: ',v2)
#    print ('——————————')
#    print ('Você tirou um C!')
#    print ('Sua media é de: ',nota)
#    print ('você foi aprovado!!')
#elif nota >= 4 and nota < 6:
#    print ('A nota da primeira prova: ',v1)
#    print ('A nota da segunda prova: ',v2)
#    print ('——————————')
#    print ('Você tirou um D!')
#    print ('Sua media é de: ',nota)
#    print ('você foi Reprovado!!')
#elif nota < 4:
#    print ('A nota da primeira prova: ',v1)
#    print ('A nota da segunda prova: ',v2)
#    print ('——————————')
#    print ('Você tirou um E!')
#    print ('Sua media é de: ',nota)
#    print ('você foi Reprovado!!')
'''15 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''
#l1 = int(input("Lado 1: "))
#l2 = int(input("Lado 2: "))
#l3 = int(input("Lado 3: "))
#if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
#	print ("Não pode ser um triangulo")
#elif l1 == l2 == l3:
#	print ("Equilatero")
#elif l1 == l2 or l1 == l3 or l2 == l3:
#	print ("Isósceles")
#else:
#	print ("Escaleno")
'''16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''
#print('Equaçao do 2o grau da forma: ax² + bx + c')
#a = int( input('Coeficiente a: ') )
#if(a==0):
#    print('Se a=0, não é equação do segundo grau. ')
#else:
#    b = int( input('Coeficiente b: ') )
#    c = int( input('Coeficiente c: ') )
#    delta = b*b - (4*a*c)
#if delta<0:
#    print('Delta menor que 0. Raízes imaginárias. ')
#elif delta==0:
#    raiz = -b / (2*a)
#    print('Delta=0 , raiz = ',raiz)
#else:
#    raiz1 = (-b + math.sqrt(delta) ) / (2*a)
#    raiz2 = (-b - math.sqrt(delta) ) / (2*a)
#    print('Raizes: ',raiz1,' e ',raiz2)
'''17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.''' 
#ano = int(input("digite um ano (XXXX): "))
#if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
#    print (ano, " O ano informado é Bissexto")
#else:
#    print (ano, " O ano informado não é bissexto")
'''18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''
#data = input("digite uma data com o seguinte formato dd/mm/aaaa ---> ")
#dia = int(data[0:2])
#mes = int(data[3:5])
#ano = int(data[6:10])
#validade = "true"
#i = 0
#while validade == "true" and i == 0:
#    if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
#        bissexto = "sim"
#    else:
#        bissexto = "nao"
#    if mes < 1 or mes > 12:
#        validade = "false"
#    if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
#        validade = "false"
#    if (mes == 2 and bissexto == "nao" and dia > 28) or ( mes == 2 and bissexto == "sim" and dia > 29):
#        validade = "false"
#    i = i + 1
#if validade == "true":
#    print("data valida")
#else:
#    print("data invalida")
'''19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''
#numero = input("digite um numero menor que 1000 ---> ")
#numeroStr = str(numero)
#qtNumero = len(numeroStr)
#if qtNumero == 3:
#    centena = numeroStr[0:1]
#    dezena = numeroStr[1:2]
#    unidade = numeroStr[2:3]
#    print (numeroStr+" = "+centena+" centenas , "+dezena+" dezenas, "+unidade+ " unidades")
#if qtNumero == 2:
#    dezena = numeroStr[0:1]
#    unidade = numeroStr[1:2]
#    print (numeroStr+" = "+dezena+" dezenas, "+unidade+ " unidades")
#if qtNumero == 1:
#    unidade = numeroStr[0:1]
#    print (numeroStr+" = "+unidade+ " unidades")
'''20 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''
#saque = int(input("Digite o valor do saque: "))
#if 10 <= saque <= 600:
#    notas_cem = saque // 100
#    saque = saque % 100
#    notas_cinquenta = saque // 50
#    saque = saque % 50
#    notas_dez = saque // 10
#    saque = saque % 10
#    notas_cinco = saque // 5
#    saque = saque % 5
#    notas_um = saque // 1
#    if notas_cem > 0:
#        print(notas_cem, "notas de R$ 100")
#    if notas_cinquenta > 0:
#        print(notas_cinquenta, "notas de R$ 50")
#    if notas_dez > 0:
#        print(notas_dez, "notas de R$ 10")
#    if notas_cinco > 0:
#        print(notas_cinco, "notas de R$ 5")
#    if notas_um > 0:
#        print(notas_um, "notas de R$ 1")
#else:
#    print("Nao é possivel fazer o saque")
'''21 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).'''
#num = int(input("Insira um número inteiro: "))
#if num % 2 == 0:
#    print(num, " é par")
#else:
#    print(num, " é ímpar")
'''22 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.''' 
#num = float(input("Informe um número: "))
#if num //1 == num:
#  print("Número inteiro")
#else:
#  print("Número Decimal")  
'''23 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''
#num1 = float(input("Digite o primeiro numero: "))
#operacao = input("Qual operacao voce deseja? (1 - par ou ímpar , 2 -positivo ou negativo , 3 -inteiro ou decimal): ")
#if operacao == 1:
#   if num1 % 2 == 0:
#        print(num1, " é par")
#    else:
#        print(num1, " é ímpar")
#    if num2 % 2 == 0:
#        print(num2, " é par")
#    else:
#        print(num2, " é ímpar")
#if operacao == 2:
#    if num1 //1 == num1:
#      print("Número inteiro")
#    else:
#      print("Número Decimal") 
#    if num2 //1 == num2:
#      print("Número inteiro")
#    else:
#      print("Número Decimal") 
#if operacao == 3:
#    if num1 //1 == num1:
#      print("Número inteiro")
#    else:
#      print("Número Decimal") 
#    if num2 //1 == num2:
#      print("Número inteiro")
#    else:
#      print("Número Decimal") 
'''24 - aça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''
a = int(input('Telefonou para a vítima? \n1 - Sim \n2 -Não\n'))
b = int(input('Esteve no local do crime? \n1 - Sim \n2 -Não\n'))
d = int(input('Mora perto da vítima? \n1 - Sim \n2 -Não\n'))
c = int(input('Devia para a vítima? \n1 - Sim \n2 -Não\n'))
e = int(input('Já trabalhou com a vítima?\n 1 - Sim \n2 -Não\n'))
soma = a+b+c+d+e
if(soma == 2):
    print('Suspeita')
elif(soma == 3 or soma == 4):
    print('Cúmplice')
elif(soma ==5):
    print('Assassino')    
else:
    print('Inocente')
