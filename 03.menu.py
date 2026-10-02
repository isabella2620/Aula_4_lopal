

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
