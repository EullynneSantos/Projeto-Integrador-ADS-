import random

def jogar_jogo():
    numero_secreto = random.randint(1, 100)
    numero_tentativas = 0
    tentativas_maximas = 10

    print("Bem-vindo ao jogo de adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    while numero_tentativas < tentativas_maximas:
        palpite = int(input("Digite seu palpite: "))

        numero_tentativas += 1

        if palpite < numero_secreto:
            print("Seu palpite é muito baixo.")
        elif palpite > numero_secreto:
            print("Seu palpite é muito alto.")
        else:
            print("Parabéns! Você acertou o número secreto em", numero_tentativas, "tentativas.")
            return

    print("Suas tentativas acabaram. O número secreto era", numero_secreto)

jogar_jogo()
