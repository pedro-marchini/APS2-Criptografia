import os

# str alfabeto com as letras e acentuações
alfabeto: str = "aáàãâbcçdeéèêfghiíìîjklmnoóòõôpqrstuúùûvwxyzAÁÀÃÂBCDEÉÈÊFGHIÍÌÎJKLMNOÓÒÕÔPQRSTUÚÙÛVWXYZ"

# Define uma variável para armazenar a opção escolhida pelo usuário
tipoConversao = None

# laço para repetir o menu, fazendo com que o usuário saia digitando 3.
while tipoConversao != "":
    # Limpa a tela
    os.system("cls")

    # Exibe as opções disponíveis
    print("Escolha uma opção:")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    print("0 - Sair")

    # Lê a opção escolhida pelo usuário
    tipoConversao = input()

    # Verifica a opção escolhida
    if tipoConversao == "0":
        # Limpa a tela
        os.system("cls")
        # Espera o usuário pressionar Enter
        input('Digite "enter" para encerrar...')
        # Encerra o fluxo
        break
    # Verifica se a opção escolhida é 1 ou 2, caso seja diferente, volta para o começo do while.
    elif tipoConversao != "1" and tipoConversao != "2":
        # Limpa a tela
        os.system("cls")
        print("Código inválido.")
        # Espera o usuário pressionar Enter
        input()
        continue

    # Limpa a tela
    os.system("cls")
    # str mensagem
    mensagem: str = input("Digite uma mensagem: ")
    # Limpa a tela
    os.system("cls")

    # chave int (valor dentro de 1 até o tamanho do alfabeto - 1)
    chave: int = int(input("Digite a chave entre 1 e {0}: ".format(len(alfabeto) - 1)))
    # Limpa a tela
    os.system("cls")

    # enquanto a chave digitada estiver incorreta solicita novamente
    while chave < 1 or chave > len(alfabeto) - 1:
        # Limpa a tela
        os.system("cls")
        print("chave inválida")
        chave = int(input("Digite a chave entre 1 e {0}: ".format(len(alfabeto) - 1)))

    # str mensagemConvertida, onde ficará a mensagem após ser criptografada ou descriptografada
    mensagemConvertida: str = ""

    # laço para percorrer o texto digitado
    for c in mensagem:
        # verifica se existe o caracter em questão no alfabeto
        if c in alfabeto:
            # aqui existe o caractere
            # encontra o indice (posição) da letra no alfabeto
            indice = alfabeto.find(c)

            # se 1 é para criptografar
            if tipoConversao == "1":
                # então soma-se o valor da chave ao indice
                indice = indice + chave
            # se 2 é para decriptografar
            elif tipoConversao == "2":
                # então subtrai-se o valor da chave ao indice
                indice = indice - chave

            # se novo indice é maior ou igual ao tamanho do alfabeto rotacionar
            if indice >= len(alfabeto):
                # reduzo o tamanho do alfabeto no indice voltando ao início do alfa
                indice -= len(alfabeto)
            # se novo indice é menor que 0 rotacionar
            elif indice < 0:
                # aumento o tamanho do alfabeto no indice indo ao final do alfa
                indice += len(alfabeto)
            # adiciono o caractere da posição indice já ajustada ao novo texto
            mensagemConvertida += alfabeto[indice]
        # se não existir cópia, o mesmo caracter para mensagemConvertida
        else:
            mensagemConvertida += c

    # se a o tipo de conversão for criptografia ou descriptografia, executa o bloco de código abaixo
    if tipoConversao == "1" or tipoConversao == "2":
        # Limpa a tela
        os.system("cls")
        # imprime a mensagem convertida (criptografado ou decriptografado)
        print(mensagemConvertida)
        # Espera o usuário pressionar Enter
        input('Pressione "enter" para continuar...')