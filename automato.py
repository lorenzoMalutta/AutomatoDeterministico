# Manipulador recebe o arquivo em formato de texto para somente leitura.
manipulador = open('entrada.txt', 'r')

saída = open('saida.txt', "w")
print("\n0 - erro\n1 - aceito")
print("\nApenas os  símbolos a b c são válidos.")
print('\nApenas palavras com um número par de caracteres seram aceitas.')
print('\nEntradas: ')

# Mostra a leitura do arquivo
print(manipulador.read())

# O comando with certifica que o arquivo ira abrir e fechar.
with open('entrada.txt') as texto:
    linha = texto.readlines()

    print("\nA saída respectivamente:")

    # For para separar cada palavra.
    for palavra in linha:
        # O cont para contar cada letra e reseta após a quebra de linha.
        cont = 0
        # Letra recebe palavra em forma de lista ordenada para melhor organização.
        letra = sorted(palavra)
        # O for para ler letra por letra e validar se pertence ao alfabeto de a b c
        for caracter in letra[0:]:
            if "a" in caracter:
                cont += 1
            elif "b" in caracter:
                cont += 1
            elif "c" in caracter:
                cont += 1
            # Este elif serve para nao contar os espaços vazios e as quebras de linhas como caracteres
            elif " " or "\n" in caracter:
                cont += 0
        # O cont != 0 serve para não contar o zero como par, poís caso coloque um caracter diferente do permitido
        # o programa ira reconhecer como zero.
        # A saída.write escreve os resultados em outro arquivo de saida.
        if cont % 2 == 0 and cont != 0:
            saída.write("1\n")
            print("Aceito!")
        else:
            saída.write("0\n")
            print("Erro!")

# Fechando o arquivo
manipulador.close()
