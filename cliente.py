from socket import *
from http import *
from weakref import *
from xmlrpc.server import *
import xmlrpc.client


proxy = xmlrpc.client.ServerProxy('http://localhost:6789')
#multicall = xmlrpc.client.MultiCall(proxy)

print("O que você deseja:\n Soma = +\n Subtracao = -\n Multiplicacao = *\n Divisao = /\n ")

while True:

    opcao = input("\nDigite a opção escolhida:")
    num1 = float(input("Digite o primeiro numero:"))
    num2 = float(input("Digite o segundo numero:"))

    if opcao == '+':
        print(f"operação: {num1} {opcao} {num2} = {proxy.som(num1,num2)} ")

    elif opcao == '-':
        print(f"operação: {num1} {opcao} {num2} = {proxy.sub(num1,num2)} ")

    elif opcao == '*':
        print(f"operação: {num1} {opcao} {num2} = {proxy.mult(num1,num2)} ")    

    elif opcao == '/':
        print(f"operação: {num1} {opcao} {num2} = {proxy.div(num1,num2)} ")

    else:
        print("Operação inválida")