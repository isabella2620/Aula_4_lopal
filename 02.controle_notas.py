nome = input("Digite o nome: ")
nota = float(input("Qual a nota? "))

quantidade_de_notas = 1
soma_das_notas = nota

pergunta = input("Quer adicionar uma nota? ")

while pergunta == "sim":
    nota = float(input("Qual a nota? "))
    soma_das_notas = soma_das_notas + nota
    quantidade_de_notas = quantidade_de_notas + 1
    
    pergunta = input("Quer adicionar uma nota? ")

media = soma_das_notas / quantidade_de_notas

if media >= 5:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"Nome: {nome}")
print(f"Media: {media}")
print(f"Situacao: {situacao}")
