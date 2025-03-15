# Criando um dicionário
meu_dicionario = {
  'nome': 'João',
  'idade': 25,
  'cidade': 'São Paulo'
}

# Acessando valores
print(meu_dicionario['nome'])  # Saída: João
print(meu_dicionario.get('idade'))  # Saída: 25

# Adicionando novos pares chave-valor
meu_dicionario['profissao'] = 'Engenheiro'
print(meu_dicionario)

# Atualizando valores
meu_dicionario['idade'] = 26
print(meu_dicionario)

# Removendo pares chave-valor
del meu_dicionario['cidade']
print(meu_dicionario)

# Iterando sobre um dicionário
for chave, valor in meu_dicionario.items():
  print(f'{chave}: {valor}')

# Métodos úteis
chaves = meu_dicionario.keys()
valores = meu_dicionario.values()
itens = meu_dicionario.items()

print(chaves)  # Saída: dict_keys(['nome', 'idade', 'profissao'])
print(valores)  # Saída: dict_values(['João', 26, 'Engenheiro'])
print(itens)  # Saída: dict_items([('nome', 'João'), ('idade', 26), ('profissao', 'Engenheiro')])

# Verificando a existência de uma chave
if 'nome' in meu_dicionario:
  print('A chave "nome" existe no dicionário.')

# Limpando o dicionário
meu_dicionario.clear()
print(meu_dicionario)  # Saída: {}