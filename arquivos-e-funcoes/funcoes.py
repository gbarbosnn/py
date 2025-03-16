# Material de Estudos: Funções em Python

# Definição de Função
# Uma função é um bloco de código que só é executado quando é chamado.
# Você pode passar dados, conhecidos como parâmetros, para uma função.
# Uma função pode retornar dados como resultado.

# Exemplo de uma função simples
def saudacao():
  print("Olá, Mundo!")

# Chamando a função
saudacao()

# Função com Parâmetros
def saudacao_personalizada(nome):
  print(f"Olá, {nome}!")

# Chamando a função com um argumento
saudacao_personalizada("Gabriel")

# Função com Retorno
def soma(a, b):
  return a + b

# Chamando a função e armazenando o resultado
resultado = soma(5, 3)
print(f"A soma é: {resultado}")

# Função com Parâmetros Padrão
def saudacao_com_idade(nome, idade=30):
  print(f"Olá, {nome}! Você tem {idade} anos.")

# Chamando a função com e sem o parâmetro idade
saudacao_com_idade("Gabriel")
saudacao_com_idade("Gabriel", 25)

# Função com Número Variável de Argumentos
def lista_de_compras(*itens):
  print("Itens da lista de compras:")
  for item in itens:
    print(f"- {item}")

# Chamando a função com múltiplos argumentos
lista_de_compras("Maçã", "Banana", "Laranja")

# Função com Argumentos Nomeados
def exibir_informacoes(nome, idade):
  print(f"Nome: {nome}, Idade: {idade}")

# Chamando a função com argumentos nomeados
exibir_informacoes(idade=25, nome="Gabriel")

# Funções Lambda
# Funções lambda são pequenas funções anônimas que podem ter qualquer número de argumentos, mas apenas uma expressão.
soma_lambda = lambda a, b: a + b
print(f"A soma usando lambda é: {soma_lambda(5, 3)}")