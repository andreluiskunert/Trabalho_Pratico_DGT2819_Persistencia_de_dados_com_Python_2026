# ============================================================
# TRABALHO PRÁTICO - DGT2819
# Persistência de dados com Python
# Projeto: Colocando tudo em ordem e guardando
# ============================================================

import time


def bubble_sort(array):
    """Ordena a lista usando o algoritmo Bubble Sort."""
    for i in range(len(array) - 1):
        trocou = False

        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                trocou = True

        if not trocou:
            break


def selection_sort(array):
    """Ordena a lista usando o algoritmo Selection Sort."""
    for i in range(len(array) - 1):
        menor = i

        for j in range(i + 1, len(array)):
            if array[j] < array[menor]:
                menor = j

        if menor != i:
            array[i], array[menor] = array[menor], array[i]


# ============================================================
# LEITURA DO ARQUIVO
# ============================================================

palavras = []

with open("documento.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        palavras.extend(linha.split())


# ============================================================
# REMOÇÃO DE CARACTERES
# ============================================================

palavras_limpa = []

for palavra in palavras:
    palavra = palavra.strip(".,;:!?()[]{}\"'")
    if palavra:
        palavras_limpa.append(palavra)

palavras = palavras_limpa


# ============================================================
# EXECUÇÃO E COMPARAÇÃO DOS ALGORITMOS
# ============================================================

lista_bubble = palavras.copy()
inicio_bubble = time.perf_counter()
bubble_sort(lista_bubble)
fim_bubble = time.perf_counter()
tempo_bubble = fim_bubble - inicio_bubble

lista_selection = palavras.copy()
inicio_selection = time.perf_counter()
selection_sort(lista_selection)
fim_selection = time.perf_counter()
tempo_selection = fim_selection - inicio_selection

lista_sort = palavras.copy()
inicio_sort = time.perf_counter()
lista_sort.sort()
fim_sort = time.perf_counter()
tempo_sort = fim_sort - inicio_sort


# ============================================================
# EXIBIÇÃO DOS RESULTADOS
# ============================================================

print("=" * 60)
print("TRABALHO PRÁTICO - DGT2819")
print("PERSISTÊNCIA DE DADOS COM PYTHON")
print("=" * 60)

print(f"\nQuantidade de palavras encontradas: {len(palavras)}")

print("\nPrimeiras palavras encontradas:")
print(palavras[:20])

print("\n" + "=" * 60)
print("COMPARAÇÃO DOS ALGORITMOS")
print("=" * 60)

print(f"\nBubble Sort:    {tempo_bubble:.10f} segundos")
print(f"Selection Sort: {tempo_selection:.10f} segundos")
print(f"Sort Python:    {tempo_sort:.10f} segundos")


# Verifica se os três métodos produziram o mesmo resultado.
if lista_bubble == lista_selection == lista_sort:
    print("\nVerificação: os três métodos produziram o mesmo resultado.")
else:
    print("\nAtenção: os resultados dos métodos são diferentes.")


tempos = {
    "Bubble Sort": tempo_bubble,
    "Selection Sort": tempo_selection,
    "Sort Python": tempo_sort,
}

melhor_metodo = min(tempos, key=tempos.get)

print(f"\nMétodo com menor tempo de execução: {melhor_metodo}")
print(f"Tempo de execução: {tempos[melhor_metodo]:.10f} segundos")


# ============================================================
# PERSISTÊNCIA DO RESULTADO
# ============================================================

# O arquivo final usa o resultado do sort() nativo do Python.
with open("palavras_ordenadas.txt", "w", encoding="utf-8") as arquivo:
    for palavra in lista_sort:
        arquivo.write(palavra + "\n")

print("\nArquivo 'palavras_ordenadas.txt' criado com sucesso!")
print("Programa finalizado.")
