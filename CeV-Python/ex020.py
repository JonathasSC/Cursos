#embaralha itens de uma lista 
import random
nomes = input("Informe o nome de todos os alunos: ")
lista = nomes.split(" ,")
random.shuffle(lista)
print(f"a ordem ficou {lista}")
aleatório = random.choice(lista)
print(f"o escolhido foi: {aleatório}")

