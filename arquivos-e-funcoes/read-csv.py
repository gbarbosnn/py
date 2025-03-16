import csv

# Define o caminho para o arquivo CSV
caminho_arquivo: str = './exemplo.csv'

# Inicializa uma lista vazia para armazenar os dados
dados: list = []

# Abre o arquivo CSV para leitura
with open(file=caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
  # Cria um objeto leitor de CSV que lerá o arquivo como um dicionário
  leitor_csv = csv.DictReader(arquivo)

  # Itera sobre cada linha no arquivo CSV
  for linha in leitor_csv:
    # Adiciona cada linha (como um dicionário) à lista
    dados.append(linha)

# Itera sobre a lista de dicionários e imprime cada um
for registro in dados:
  print(registro)