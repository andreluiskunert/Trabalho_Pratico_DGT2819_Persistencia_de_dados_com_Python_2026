# Microatividade 5
# Escrita de dados em arquivo externo

arquivo = open("texto.txt", "w", encoding="utf-8")

texto = list()

texto.append("Python é uma linguagem de programação.")
texto.append("Python permite trabalhar com arquivos.")
texto.append("Python possui diversos algoritmos de ordenação.")
texto.append("A persistência de dados é importante para aplicações.")
texto.append("Este arquivo foi criado automaticamente pelo programa.")

for frase in texto:

    arquivo.write(frase + "\n")

arquivo.close()

print("Arquivo texto.txt criado com sucesso!")