# Microatividade 3
# Ordenação utilizando o algoritmo Selection Sort

array = [
    64, 25, 12, 22, 11,
    90, 34, 7, 56, 43,
    18, 72, 5, 81, 30
]

print("Array original:")
print(array)


for i in range(len(array)):

    menor = i

    for j in range(i + 1, len(array)):

        if array[menor] > array[j]:

            menor = j

    auxiliar = array[i]

    array[i] = array[menor]

    array[menor] = auxiliar


print("\nArray ordenado utilizando Selection Sort:")
print(array)