# Microatividade 1
# Ordenação de arrays utilizando o método sort() do Python

# Array com 15 números inteiros
numeros = [45, 12, 78, 3, 56, 23, 89, 1, 34, 67, 90, 15, 8, 42, 29]

print("Array original:")
print(numeros)

# Ordenação crescente
numeros.sort()

print("\nArray ordenado de forma crescente:")
print(numeros)

# Ordenação decrescente
numeros.sort(key=None, reverse=True)

print("\nArray ordenado de forma decrescente:")
print(numeros)


# Array de strings
pessoas = [
    "Carlos",
    "Andre",
    "Bruno",
    "Daniel",
    "Eduardo",
    "Fernanda",
    "Gabriel",
    "Helena",
    "Isabela",
    "Joao",
    "Karina",
    "Lucas",
    "Marcos",
    "Natalia",
    "Paulo"
]

print("\nArray de nomes original:")
print(pessoas)

# Ordem crescente
pessoas.sort()

print("\nNomes em ordem crescente:")
print(pessoas)

# Ordem decrescente
pessoas.sort(key=None, reverse=True)

print("\nNomes em ordem decrescente:")
print(pessoas)