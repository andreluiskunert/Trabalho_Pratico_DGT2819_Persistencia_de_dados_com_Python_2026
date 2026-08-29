# Microatividade 2
# Ordenação utilizando o algoritmo Bubble Sort

def bubbleSort(array):

    for i in range(len(array)):

        for j in range(0, len(array) - i - 1):

            if array[j] > array[j + 1]:

                auxiliar = array[j]

                array[j] = array[j + 1]

                array[j + 1] = auxiliar


# Array com 15 números
numeros = [
    64, 25, 12, 22, 11,
    90, 34, 7, 56, 43,
    18, 72, 5, 81, 30
]

print("Array original:")
print(numeros)

bubbleSort(numeros)

print("\nArray ordenado utilizando Bubble Sort:")
print(numeros)