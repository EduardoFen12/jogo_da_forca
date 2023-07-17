#===================================================================================================

from functions import *
import random

#===================================================================================================


# VARIÁVEIS:


# Lista da palavras do jogo:
lista = ["computacao", 
         "ciencia", 
         "python", 
         "programacao", 
         "scratch", 
         "machine learning", 
         "logica de programacao", 
         "calendario", 
         "signo chines", 
         "gremio maior do mundo"]


# Vesões da forca para vidas restantes
desenhos = [" +---+  \n |   |  \n |      \n |      \n |      \n |      \n=========",
            " +---+  \n |   |  \n |   0  \n |      \n |      \n |      \n=========",
            " +---+  \n |   |  \n |   0  \n |   |  \n |      \n |      \n=========",
            " +---+  \n |   |  \n |   0  \n |  /|  \n |      \n |      \n=========",
            " +---+  \n |   |  \n |   0  \n |  /|\\\n |      \n |      \n=========",
            " +---+  \n |   |  \n |   0  \n |  /|\\\n |  /   \n |      \n=========",
            " +---+  \n |   |  \n |   0  \n |  /|\\\n |  / \\\n |      \n========="]

# Contador de vidas perdidas
vidas = 0

# Conjunto com as respostas do usuário
respostas = set()

# Contador de acertos
nro_acertos = 0

# Sorteia a palavra para o jogo:
palavra = random.choice(lista)

#tamanho da palavra secreta sem os espaços
tamanho_palavra = len(palavra) - palavra.count(" ")


#===================================================================================================


# INÍCIO DO JOGO:


regras()

while vidas < 6:

    mostra_palavra(palavra, respostas)
    print("\n\n")

    # Lê a resposta do usuário
    r = input("\nDigite uma letra: ")

    # Verifica se a resposta é válida
    r_valida = verifica_resposta(r, respostas)

    if r in palavra and r_valida == True:

        respostas.add(r)

        print("Acertou!!!")

        nro_acertos += palavra.count(r)

        if tamanho_palavra == nro_acertos:
            print(f"### PARABÉNS, você ganhou :) ###\aA resposta era {palavra}")
            vidas = 6

    else:

        if r_valida == True:

            vidas +=1

            if vidas < 6:

                print(f"Uhhh!!! Vidas restantes: {6 - vidas}")

            else:

                print(f"### Você Perdeu :( ###\aA resposta era {palavra}")
                print(desenhos[vidas])
                mostra_palavra(palavra, respostas)
                print("\n\n")

    if vidas < 6:
        print(desenhos[vidas])


#===================================================================================================