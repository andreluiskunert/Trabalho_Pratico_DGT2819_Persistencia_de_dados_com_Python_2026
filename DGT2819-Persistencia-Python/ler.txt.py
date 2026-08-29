# Microatividade 4
# Leitura de dados de um arquivo externo

# Abrindo o arquivo
arquivo = open("loremipsum.txt", "r", encoding="utf-8")

# Lendo todo o conteúdo
conteudo = arquivo.read()

print("CONTEÚDO COMPLETO DO ARQUIVO:")
print(conteudo)

# Fechando o arquivo
arquivo.close()


# Abrindo novamente para ler a primeira linha
arquivo = open("loremipsum.txt", "r", encoding="utf-8")

primeira_linha = arquivo.readline()

print("\nPRIMEIRA LINHA:")
print(primeira_linha)

arquivo.close()


# Lendo os três primeiros caracteres
arquivo = open("loremipsum.txt", "r", encoding="utf-8")

tres_caracteres = arquivo.read(3)

print("\nTRÊS PRIMEIROS CARACTERES:")
print(tres_caracteres)

arquivo.close()


# Utilizando with
print("\nLEITURA UTILIZANDO WITH:")

with open("loremipsum.txt", "r", encoding="utf-8") as arquivo:

    conteudo = arquivo.read()

    print(conteudo)