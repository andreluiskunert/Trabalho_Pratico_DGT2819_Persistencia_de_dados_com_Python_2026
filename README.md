# 🐍 DGT2819 - Persistência de Dados com Python

## 📚 Sobre o projeto

Este projeto foi desenvolvido como trabalho prático da disciplina **DGT2819 - Persistência de Dados com Python**.

O objetivo é aplicar conceitos de manipulação de arquivos e algoritmos de ordenação utilizando Python.

O programa realiza a leitura de um arquivo de texto, separa seu conteúdo em palavras, armazena essas palavras em uma lista e compara diferentes métodos de ordenação.

## 🎯 Objetivos

O projeto permite praticar:

* Manipulação de listas em Python;
* Leitura de arquivos `.txt`;
* Escrita de arquivos `.txt`;
* Utilização do método nativo `sort()`;
* Implementação do algoritmo **Bubble Sort**;
* Implementação do algoritmo **Selection Sort**;
* Medição do tempo de execução dos algoritmos;
* Comparação de desempenho entre os métodos de ordenação.

## ⚙️ Como o projeto funciona

O funcionamento do projeto ocorre nas seguintes etapas:

```text
Arquivo TXT
    ↓
Leitura do arquivo
    ↓
Leitura linha por linha
    ↓
Separação das palavras
    ↓
Armazenamento em uma lista
    ↓
Ordenação das palavras
    ├── Bubble Sort
    ├── Selection Sort
    └── sort() do Python
    ↓
Comparação do tempo de execução
    ↓
Escolha do método com melhor desempenho
    ↓
Geração do arquivo TXT com as palavras ordenadas
```

## 🗂️ Estrutura do projeto

Uma possível organização dos arquivos é:

```text
DGT2819-Persistencia-Python/
│
├── kdd.py
├── arquivo.txt
├── palavras_ordenadas.txt
├── bubble.sort.py
├── selection.sort.py
├── array.sort.py
├── ler.txt.py
├── escrever.txt.py
└── README.md
```

### 📄 Principais arquivos

**`kdd.py`**

É o arquivo principal do trabalho prático. Ele realiza a leitura do arquivo `.txt`, separa o conteúdo em palavras, executa os métodos de ordenação e compara o tempo de execução.

**`bubble.sort.py`**

Contém a implementação do algoritmo **Bubble Sort**, que compara elementos adjacentes e realiza trocas para colocar os valores em ordem crescente.

**`selection.sort.py`**

Contém a implementação do **Selection Sort**, que procura o menor elemento e o posiciona na posição correta da lista.

**`array.sort.py`**

Demonstra a utilização do método nativo `sort()` do Python para ordenar arrays.

**`ler.txt.py`**

Demonstra como realizar a leitura de dados armazenados em um arquivo de texto.

**`escrever.txt.py`**

Demonstra como criar e escrever informações em um arquivo externo.

## 🔄 Algoritmos utilizados

### Bubble Sort

O Bubble Sort percorre a lista comparando elementos adjacentes. Quando um elemento está maior que o próximo, os valores são trocados.

É um algoritmo simples e indicado principalmente para listas pequenas.

### Selection Sort

O Selection Sort percorre a lista procurando o menor elemento. Depois, coloca esse elemento na posição correta e continua o processo até que toda a lista esteja ordenada.

### `sort()`

O Python possui um método nativo para ordenação de listas:

```python
lista.sort()
```

Também é possível realizar uma ordenação decrescente utilizando:

```python
lista.sort(key=None, reverse=True)
```

## ⏱️ Comparação de desempenho

O projeto utiliza a biblioteca `time` para medir o tempo necessário para cada método realizar a ordenação.

A comparação permite observar a diferença de desempenho entre:

```text
Bubble Sort
     ↓
Selection Sort
     ↓
sort() do Python
```

Após os testes, o método escolhido deve ser utilizado para gerar o arquivo final contendo as palavras ordenadas.

## 💾 Persistência de dados

A persistência é realizada através de arquivos de texto.

O projeto utiliza Python para:

1. Abrir um arquivo `.txt`;
2. Ler seu conteúdo;
3. Processar os dados;
4. Armazenar as palavras em uma lista;
5. Ordenar os dados;
6. Criar um novo arquivo;
7. Gravar as palavras ordenadas.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Visual Studio Code**
* **Git**
* **GitHub**
* Arquivos de texto `.txt`

## ▶️ Como executar

### 1. Instale o Python

Verifique se o Python está instalado:

```bash
python3 --version
```

### 2. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 3. Entre na pasta do projeto

```bash
cd DGT2819-Persistencia-Python
```

### 4. Execute o programa

```bash
python3 kdd.py
```

O programa realizará o processamento do arquivo de texto e apresentará os resultados da ordenação.

## 📊 Resultado esperado

Ao executar o projeto, serão apresentados os resultados da ordenação utilizando os diferentes métodos.

Também será apresentado o tempo de execução de cada método, permitindo comparar o desempenho entre eles.

Após a escolha do método mais adequado, o projeto deverá gerar um novo arquivo `.txt` contendo as palavras ordenadas.

## 🎓 Contexto acadêmico

Este projeto faz parte do trabalho prático da disciplina:

**DGT2819 - Persistência de Dados com Python**

A atividade tem como objetivo aplicar, de forma conjunta, conhecimentos de manipulação de arquivos e algoritmos de ordenação.

## 👨‍💻 Autor

**Andre Luis Kunert**

Projeto desenvolvido para fins acadêmicos.

---

⭐ Projeto desenvolvido durante os estudos de **Python, algoritmos de ordenação e persistência de dados**.
Obs.: corrigido..
