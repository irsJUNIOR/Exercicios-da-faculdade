# Primeiro exercicio da faculdade baseado em python##
# Aqui vou calcular a porcentagem de uma garagem dentro de um terreno
# Aqui vou nomear a variavel e usar o comando float para interpretar a entrada
# de texto que o comando input irá solicitar, de forma numérica.

Largura_garagem = float(input("Entre com a largura da garagem em metros:"))

Profundidade_garagem = float(
    input("Entre com a profundidade da garagem em metros:"))

# Abaixo será calculado o valor da área da garagem

Area_garagem = Largura_garagem * Profundidade_garagem


# --------------------------------------------------------------------------


Largura_terreno = float(input("Entre com a largura do terreno em metros:"))

Profundidade_terreno = float(
    input("Entre com a profundidade do terreno em metros:"))

# Abaixo será calculado o valor da área do terreno

Area_terreno = Largura_terreno * Profundidade_terreno

# Agora, calcularemos o percentual de ocupação da garagem sobre o terreno
# Aqui irei usar as variaveis criadas, onde de seus valores serão usados
# em uma equação matemática,
# descobrindo a area de ocupação em percentual da garagem sobre o terreno


Percentual = ((Area_garagem) / (Area_terreno)) * 100
print("Percentual de ocupação: ", Percentual)

# LEIA ANTES DE EXECUTAR O EXERCICIO
# largura = l    //    profundidade = p
# garagem l=5 p=6  terreno l=20 p=20
# se tudo ocorrer bem o resultado esperado é de 7,5%.
