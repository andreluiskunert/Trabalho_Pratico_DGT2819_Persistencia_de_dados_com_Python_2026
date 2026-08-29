# # ============================================================
# # TRABALHO PRÁTICO - DGT2819
# # Persistência de dados com Python
# #
# # Projeto: Colocando tudo em ordem e guardando
# # ============================================================

# import time


# # ============================================================
# # BUBBLE SORT
# # ============================================================

# def bubble_sort(array):

#     for i in range(len(array)):

#         for j in range(0, len(array) - i - 1):

#             if array[j] > array[j + 1]:

#                 auxiliar = array[j]

#                 array[j] = array[j + 1]

#                 array[j + 1] = auxiliar


# # ============================================================
# # SELECTION SORT
# # ============================================================

# def selection_sort(array):

#     for i in range(len(array)):

#         menor = i

#         for j in range(i + 1, len(array)):

#             if array[menor] > array[j]:

#                 menor = j

#         auxiliar = array[i]

#         array[i] = array[menor]

#         array[menor] = auxiliar


# # ============================================================
# # LEITURA DO ARQUIVO
# # ============================================================

# palavras = list()


# with open("documento.txt", "r", encoding="utf-8") as arquivo:

#     for linha in arquivo:

#         palavras_linha = linha.split()

#         palavras.extend(palavras_linha)


# # ============================================================
# # REMOÇÃO DE CARACTERES
# # ============================================================

# palavras_limpa = list()


# for palavra in palavras:

#     palavra = palavra.strip(".,;:!?()[]{}\"'")

#     if palavra:

#         palavras_limpa.append(palavra)


# palavras = palavras_limpa


# # ============================================================
# # EXIBIÇÃO DAS INFORMAÇÕES
# # ============================================================

# print("=" * 60)
# print("TRABALHO PRÁTICO - DGT2819")
# print("PERSISTÊNCIA DE DADOS COM PYTHON")
# print("=" * 60)

# print("\nQuantidade de palavras encontradas:")

# print(len(palavras))


# print("\nPrimeiras palavras encontradas:")

# print(palavras[:20])


# # ============================================================
# # BUBBLE SORT
# # ============================================================

# lista_bubble = palavras.copy()

# inicio_bubble = time.perf_counter()

# bubble_sort(lista_bubble)

# fim_bubble = time.perf_counter()

# tempo_bubble = fim_bubble - inicio_bubble


# # ============================================================
# # SELECTION SORT
# # ============================================================

# lista_selection = palavras.copy()

# inicio_selection = time.perf_counter()

# selection_sort(lista_selection)

# fim_selection = time.perf_counter()

# tempo_selection = fim_selection - inicio_selection


# # ============================================================
# # SORT NATIVO DO PYTHON
# # ============================================================

# lista_sort = palavras.copy()

# inicio_sort = time.perf_counter()

# lista_sort.sort()

# fim_sort = time.perf_counter()

# tempo_sort = fim_sort - inicio_sort


# # ============================================================
# # RESULTADOS
# # ============================================================

# print("\n" + "=" * 60)
# print("COMPARAÇÃO DOS ALGORITMOS")
# print("=" * 60)

# print(f"\nBubble Sort:    {tempo_bubble:.10f} segundos")

# print(f"Selection Sort: {tempo_selection:.10f} segundos")

# print(f"Sort Python:    {tempo_sort:.10f} segundos")


# # ============================================================
# # VERIFICAÇÃO DOS RESULTADOS
# # ============================================================

# print("\n" + "=" * 60)
# print("RESULTADO DAS ORDENAÇÕES")
# print("=" * 60)

# print("\nBubble Sort:")
# print(lista_bubble)

# print("\nSelection Sort:")
# print(lista_selection)

# print("\nSort Python:")
# print(lista_sort)


# # ============================================================
# # ESCOLHA DO MELHOR MÉTODO
# # ============================================================

# tempos = {
#     "Bubble Sort": tempo_bubble,
#     "Selection Sort": tempo_selection,
#     "Sort Python": tempo_sort
# }

# melhor_metodo = min(tempos, key=tempos.get)

# print("\n" + "=" * 60)
# print("ANÁLISE DE PERFORMANCE")
# print("=" * 60)

# print(f"\nO método com menor tempo de execução foi: {melhor_metodo}")

# print(f"Tempo de execução: {tempos[melhor_metodo]:.10f} segundos")


# # ============================================================
# # CRIAÇÃO DO ARQUIVO FINAL
# # ============================================================

# with open("palavras_ordenadas.txt", "w", encoding="utf-8") as arquivo:

#     for palavra in lista_sort:

#         arquivo.write(palavra + "\n")


# print("\nArquivo 'palavras_ordenadas.txt' criado com sucesso!")

# print("\nPrograma finalizado.")
import time


palavras = list()


with open("documento.txt", "r", encoding="utf-8") as arquivo:

    for linha in arquivo:

        palavras.extend(linha.split())


palavras_limpa = list()

for palavra in palavras:

    palavra = palavra.strip(".,;:!?()[]{}\"'")

    if palavra:

        palavras_limpa.append(palavra)


palavras = palavras_limpa


inicio = time.perf_counter()

palavras.sort()

fim = time.perf_counter()

tempo = fim - inicio


print("Palavras ordenadas:")

for palavra in palavras:

    print(palavra)


print(f"\nTempo de execução: {tempo:.10f} segundos")


with open("palavras_ordenadas.txt", "w", encoding="utf-8") as arquivo:

    for palavra in palavras:

        arquivo.write(palavra + "\n")


print("\nArquivo palavras_ordenadas.txt criado com sucesso!")