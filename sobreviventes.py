import numpy as np

lista = []
total_alimentos = []

for i in range(5):
    nome = input()

    lista_de_alimentos = input().split()
    quantidades = list(map(int, input().split()))

    array_de_quantidades = np.array(quantidades)

    total = np.sum(array_de_quantidades)
    total_alimentos.append(total)

    sobrevivente = (nome, lista_de_alimentos, array_de_quantidades)
    lista.append(sobrevivente)

# Exibir todos os dados
print("=== SOBREVIVENTES ===")
for i in range(5):
    print(lista[i])
    print("Total:", total_alimentos[i])

# Maior coletador
maior = max(total_alimentos)
indice = total_alimentos.index(maior)
maior_coletador = lista[indice][0]

# Média
media = sum(total_alimentos) / len(total_alimentos)

# Desafio
mais_de_10 = 0
for total in total_alimentos:
    if total > 10:
        mais_de_10 += 1

print("Maior coletador:", maior_coletador)
print("Média:", media)
print("Sobreviventes com mais de 10 itens:", mais_de_10)
