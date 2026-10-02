nome = input("Digite o nome: ")
nota = float(input("Digite a nota: "))
nova_nota = (input("Quer adicionar uma nota? "))


contador = 4
nova_nota = "sim" or "nao"
media = (nota + nova_nota)

while nova_nota == "sim":
     print("Digite nova nota: ")



if nova_nota == "sim":
    nova_nota = input("Digite nova nota: ")
    situacao = print("1")
else: 
     situacao = "2"


print (f"Nome: {nome}")
print (f"Media: {media}")
print (f"Situaca: {situacao}")