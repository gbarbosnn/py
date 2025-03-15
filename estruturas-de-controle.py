# Estrutura condicional if-elif-else
idade = 20

# Verifica se a idade é menor que 18
if idade < 18:
  print("Você é menor de idade.")
# Se a idade não for menor que 18, verifica se é menor que 65
elif idade < 65:
  print("Você é adulto.")
# Se a idade não for menor que 65, executa este bloco
else:
  print("Você é idoso.")

# O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string).
# Neste caso, estamos iterando de 0 a 4 (5 iterações no total)
for i in range(5):
  print(f"Iteração {i}")

# O loop while é usado para repetir um bloco de código enquanto uma condição for verdadeira.
contador = 0
# Continua a repetir enquanto contador for menor que 5
while contador < 5:
  print(f"Contador: {contador}")
  # Incrementa o contador em 1 a cada iteração
  contador += 1