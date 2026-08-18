Python — Sobreviventes

1) Sobre o projeto
Este projeto foi desenvolvido por mim como uma atividade acadêmica de programação em Python. O objetivo é cadastrar informações de sobreviventes, organizar os dados coletados durante expedições e realizar diferentes análises sobre as quantidades de alimentos obtidas.

2) O programa realiza as seguintes operações:

Cadastro de 5 sobreviventes;
Armazenamento dos dados em uma lista principal;
Organização das informações de cada sobrevivente em tuplas;
Armazenamento das quantidades utilizando arrays do NumPy;
Cálculo do total de alimentos coletados por sobrevivente;
Identificação do sobrevivente com maior quantidade total de alimentos;
Cálculo da média de alimentos coletados pelo grupo;
Contagem dos sobreviventes que coletaram mais de 10 itens.

3) Tecnologias utilizadas e Conceitos praticados:
Python 3
NumPy
Listas
Tuplas
Arrays
Estruturas de repetição
Estruturas condicionais
Funções de processamento de dados
Manipulação e organização de dados
Índices e acesso a elementos
Cálculos estatísticos básicos

Destaque da solução
Um dos desafios do exercício foi identificar o sobrevivente que coletou a maior quantidade de alimentos e, a partir desse resultado, recuperar seu nome na lista principal.
A solução utiliza max() para encontrar o maior total e index() para localizar sua posição na lista. Essa posição é então utilizada para acessar o nome correspondente na estrutura de dados.

maior = max(total_alimentos)
indice = total_alimentos.index(maior)
maior_coletador = lista[indice][0]
