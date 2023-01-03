#Dicionário de Pessoas com 10 Entradas.
#Diogo Pacheco


pessoas = {
    "Pessoa 1": {"nome": "João", "idade": 30, "genero": "Masculino"},
    "Pessoa 2": {"nome": "Maria", "idade": 25, "genero": "Feminino"},
    "Pessoa 3": {"nome": "Carlos", "idade": 35, "genero": "Masculino"},
    "Pessoa 4": {"nome": "Ana", "idade": 22, "genero": "Feminino"},
    "Pessoa 5": {"nome": "Luis", "idade": 40, "genero": "Masculino"},
    "Pessoa 6": {"nome": "Carla", "idade": 29, "genero": "Feminino"},
    "Pessoa 7": {"nome": "Pedro", "idade": 32, "genero": "Masculino"},
    "Pessoa 8": {"nome": "Julia", "idade": 24, "genero": "Feminino"},
    "Pessoa 9": {"nome": "Mário", "idade": 28, "genero": "Masculino"},
    "Pessoa 10": {"nome": "Sandra", "idade": 33, "genero": "Feminino"}
}

for chave, valor in pessoas.items():
    print(f'Chave: {chave}')
    print(f'Nome: {valor["nome"]}')
    print(f'Idade: {valor["idade"]}')
    if valor["genero"] == "Masculino":
        print("Masculino")
    elif valor["genero"] == "Feminino":
        print("Feminino")
    else:
        print("Outro")
