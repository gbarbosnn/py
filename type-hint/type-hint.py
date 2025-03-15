# Type hint é uma funcionalidade do Python que permite indicar o tipo de dados que uma função espera receber e o tipo de dado que ela retorna. Isso ajuda a tornar o código mais legível e a evitar erros.

# Aqui, estamos definindo uma função chamada 'process_data' que recebe um parâmetro 'data'.
# O type hint 'data: dict' indica que 'data' deve ser um dicionário.
# O type hint '-> None' indica que a função não retorna nenhum valor.

def process_data(data: dict) -> None:
    # Dentro da função, estamos iterando sobre os itens do dicionário 'data'.
    for key, value in data.items():
        # Para cada par chave-valor, estamos imprimindo a chave e o valor.
        print(f"{key}: {value}")

# Exemplo de uso da função:
# Criamos um dicionário com alguns dados.
example_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Chamamos a função 'process_data' passando o dicionário 'example_data'.
# A função irá imprimir cada chave e valor do dicionário.
process_data(example_data)