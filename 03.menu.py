def somar():
   numero1 = float(input("Digite um numero: "))
   numero2 = float(input("Digite um numero: "))
   resultado = numero1 + numero2
   print(resultado)

def subtrair():
   numero1 = float(input("Digite um numero: "))
   numero2 = float(input("Digite um numero: "))
   resultado = numero1 - numero2
   print(resultado)

def multiplicacao():
   numero1 = float(input("Digite um numero: "))
   numero2 = float(input("Digite um numero: "))
   resultado = numero1 * numero2
   print(resultado)

def dividir():
   numero1 = float(input("Digite um numero: "))
   numero2 = float(input("Digite um numero: "))
   resultado = numero1 / numero2
   print(resultado)

def pares():
   quantidade = int(input("Digite a quantidade de pares: "))
   contador = 1
   par = 2
   while contador <= quantidade:
       print(par)
       par += 2
       contador += 1

def impares():
   quantidade = int(input("Digite a quantidade de impares: "))
   contador = 1
   impar = 1
   while contador <= quantidade:
       print(impar)
       impar += 2
       contador += 1

def somatorio():
   numero1 = int(input("Digite um numero: "))
   contador = 1
   resultado = 0
   while contador <= numero1:
       resultado += contador
       contador += 1
   print(resultado)

def fatorial():
   numero1 = int(input("Digite um numero: "))
   resultado = 1
   contador = 1
   while contador <= numero1:
       resultado = resultado * contador
       contador += 1
   print(resultado)


while True:
   print ("calculadora")
   print ("1 - adição")
   print ("2 - subtração")
   print ("3 - multiplicacao")
   print ("4 - divisao")
   print ("5 - pares")
   print ("6 - impares")
   print ("7 - somatorio")
   print ("8 - fatorial")
   print ("0 - sair")

   opcao = input("Escolha uma opção: ")

   if opcao == "1":
      somar()
   elif opcao == "2":
      subtrair()
   elif opcao == "3":
      multiplicacao()
   elif opcao == "4":
      dividir()
   elif opcao == "5":
      pares()
   elif opcao == "6":
      impares()
   elif opcao == "7":
      somatorio()
   elif opcao == "8":
      fatorial()
   elif opcao == "0":
      print ("Saindo do sistema...")
      break
   else:
      print ("Opçao invalida, tente novamente!!!")
