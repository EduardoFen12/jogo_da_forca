#===================================================================================================


# FUNÇÕES: 


def regras():
    print("#### Jogo da Froca ####")
    print("Regras:")
    print("- Digite uma letra de cada vez")
    print("- Não é permitido repetir letras")
    print("- Se você acertar a letra é revelada")
    print("- Se errar perde uma vida")
    print("- Você tem 6 vidas")
    print("Boa sorte!\n\n")


def verifica_resposta(resposta, listaRespostas):

    if resposta == '' or resposta == ' ':

        print("Resposta INVÁLIDA! Digite uma letra.")
        return False

    elif len(resposta) != 1:

        print("Só é permitido uma letra por tentativa!")
        return False

    elif resposta in listaRespostas:

        print(f"A letra '{resposta.upper()}' já foi escolhida! ")
        return False

    elif not resposta.isalpha():
        print("Só é permitido responder com letras!")
        return False

    else:   
        return True


def mostra_palavra(palavra, respostas):

    for char in palavra:

        if char in respostas:
            
            print(char, end=" ")

        else:
            if char == " ":

                print(" ", end=" ")
            
            else:
                print("_", end=" ")


#===================================================================================================