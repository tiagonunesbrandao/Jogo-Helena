"""
- Protótipo de jogo para treinar matemática
- Criei uma ideia durante meus estudos de Python na PUC. Minha filha Helena, de 6 anos (na época),
queria brincar comigo enquanto eu estudava. Como sabia que ela estava aprendendo subtração na escola, criei um "joguinho" para nos distrairmos
juntos (deixei abaixo o código original).
- Finalizado em 31 de outubro de 2022.
- @author: Tiago Brandão

****CODIGO ORIGINAL****

print("Subtraindo com a Helena!\n")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número (Menor que o primeiro): "))
resultado = n1 - n2
palpite = int(input(f"{n1} menos {n2} é: "))
if palpite == resultado:
    print("\nCERTA RESPOSTA! PARABÉNS! ")
else:
    print("\nOh não, você errou! Tente novamente! ")

"""

from time import sleep
from random import choice
from random import randint


def inicio():
    print("\n\033[3;30;45mTreinando Matemática com a Helena\033[m\n")
    sleep(1)
    input("\033[1;37m>>Aperte Enter para continuar\033[m")
    sleep(1)
    print("\n\033[1;31mTeste seu conhecimento, sem usar calculadora! :)\033[m\n")
    sleep(1)

    while True:
        try:
            idade = int(input("\033[1;35mPara que eu escolha um grau adequado de "
                              "dificuldade, digite sua idade: \033[m"))
            if idade < 6:
                print(f"{idade} anos! Você tem idade abaixo do recomendado!\n"
                      f"Mas se quiser continuar, peça ajuda para alguém mais velho que você :)\n"
                      f"Lembre-se de não usar calculadora! :)\n")
                nivel_Facil()
                break
            elif idade == 6 or idade <= 8:
                print(f"{idade} anos! Você vai para o nível Fácil.\nVamos começar!\n"
                      f"Lembre-se de não usar calculadora! :)\n")
                nivel_Facil()
                break
            elif idade == 9 or idade <= 13:
                print(f"{idade} anos! Você vai para o nível Médio.\nVamos começar!\n"
                      f"Lembre-se de não usar calculadora! :)\n")
                nivel_Medio()
                break
            elif idade == 14 or idade <= 16:
                print(f"{idade} anos! Você vai para o nível Difícil.\nVamos começar!\n"
                      f"Lembre-se de não usar calculadora! :)\n")
                nivel_Dificil()
                break
            elif idade > 16:
                print(f"{idade} anos! Seu desafio será maior, nível Super Difícil!\nVamos começar!\n"
                      f"Lembre-se de não usar calculadora! :)\n")
                nivel_SuperHard()
                break
        except ValueError:
            print("\033[1mPor favor, digite apenas números :)\n\033[m")

def nivel_Facil():
    nome = str(input("\033[1;35mDigite seu nome: \033[m").upper())
    if nome == "HELENA":
        print(f"\033[4;31m{nome}!\033[m Que nome bonito, né?! :)\n")
        sleep(1.5)
    else:
        print(f"Prazer \033[4;31m{nome}!\033[m\n")
        sleep(2)


    input('\033[4;35mVocê gosta de adição e subtração?\nVou sortear DOIS números pra você e depois escolher '
          'uma dessas duas operações para o cálculo.\033[m\033[1;37m>>Enter\033[m')
    input('\n\033[4;35mVocê terá 5 rodadas e no final, '
          'terá sua nota.\nVamos ver se está em dia com o raciocínio?\033[m\033[1;37m>>Enter\033[m')
    sleep(1.5)

    # ESCOLHA RANDOMICA DE OPERACAO E NUMEROS
    again = True
    while again:

        rodada = 0
        acertos = 0
        erros = 0
        while rodada <= 4:
            rodada += 1

            print(f"\n\033[1;30;45mRODADA {rodada}\033[m\n")
            sleep(1)
            op = ["+", "-"]
            sorteio_operacao = choice(op)

            if sorteio_operacao == "+":
                n1 = randint(0, 10)
                n2 = randint(0, 10)
                print("Escolhi \033[1;35mADIÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                add = n1 + n2
                palpite = int(
                    input(f"Se somarmos \033[1;31m{n1}\033[m com \033[1;31m{n2}\033[m qual o resultado?\nDigite: "))
                if add == palpite:
                    acertos += 1
                    print(f"\033[1;34m{add}!\033[m Certa resposta! Parabéns \033[4;31m{nome}!\033[m")
                else:
                    print(f"Ops, errou ):\nVamos lá \033[4;31m{nome}\033[m, concentre-se mais e tente novamente!")
                    erros += 1

            elif sorteio_operacao == "-":
                n1 = randint(0, 10)
                n2 = randint(0, 10)
                while True:
                    if n1 >= n2:
                        sorteados = [n1, n2]
                        break
                    else:
                        n1 = randint(0, 10)
                        n2 = randint(0, 10)
                print(f"Escolhi \033[1;35mSUBTRAÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                sub = n1 - n2
                palpite = int(
                    input(f"\033[1;31m{n1}\033[m menos \033[1;31m{n2}\033[m, é?\nDigite: "))
                if sub == palpite:
                    acertos += 1
                    print(f"\033[1;34m{sub}!\033[m Muito bem, \033[4;31m{nome}!\033[m Certa resposta!")
                else:
                    print(f"\033[4;31m{nome}\033[m, dessa vez você errou ):\nMas sei que na próxima você vai acertar!")
                    erros += 1

        print(
            f"\nVocê jogou {rodada} vezes e obteve \033[1;34m{acertos}\033[m acerto(s) e \033[1;34m{erros}\033[m erro(s).\n")
        if acertos == 5:
            print("EXCELENTE! Você acertou tudo!\n\033[3;33mNota A!!\033[m\n")
        elif acertos == 4:
            print("Muito bom! Por pouco não acertou tudo!\n\033[3;32mNota B!!\033[m\n")
        elif acertos == 3:
            print("Ficou na média... Quem sabe não melhora na próxima?\n\033[3;34mNota C!!\033[m\n")
        elif acertos == 2:
            print("2 acertos não é bom hein... :/\n\033[3;35mNota D!!\033[m\n")
        else:
            print(
                "Acho que você precisa estudar mais matemática!\nPeça ajuda para um adulto!\n\033[1;31mNota E!!\033\n[m")

        escolha_sim = input(f"Deseja jogar de novo? (S = sim /N = não)").upper()

        if escolha_sim == "S":
            rodada = 0
            print("\033[1;33mLegal, vamos lá!!\033[m")
            continue
        else:
            print(f"Obrigado por jogar, \033[4;31m{nome}!\033[m Precisando treinar matemática, só chamar!")
            break

def nivel_Medio():
    nome = str(input("\033[1;35mDigite seu nome: \033[m").upper())
    if nome == "HELENA":
        print(f"\033[4;31m{nome}!\033[m Que nome bonito, né?! :)\n")
        sleep(1.5)
    else:
        print(f"Prazer \033[4;31m{nome}!\033[m\n")
        sleep(1.5)

    input("\033[4;35mVocê gosta de adição e subtração? Prefere divisão ou multiplicação?\n"
          "Vou sortear DOIS números pra você e depois a operação matemática para o cálculo.\033[m\033[1;37m>>Enter\033[m")
    input('\n\033[4;35mVocê terá 5 rodadas e no final, terá sua nota. Vamos ver se está em dia com o raciocínio?\n'
          'Você está em um nível médio de dificuldade, não se assuste com os cálculos!\nMantenha'
          ' a calma e concentração que dará tudo certo!\033[m\033[1;37m>>Enter\033[m')
    sleep(1.5)

    # ESCOLHA RANDOMICA DE OPERACAO E NUMEROS
    again = True
    while again:

        rodada = 0
        acertos = 0
        erros = 0
        while rodada <= 4:
            rodada += 1

            print(f"\n\033[1;30;45mRODADA {rodada}\033[m\n")
            sleep(1)
            op = ["+", "-", "*", "/"]
            sorteio_operacao = choice(op)

            if sorteio_operacao == "+":
                n1 = randint(0, 100)
                n2 = randint(0, 100)
                print("Escolhi \033[1;35mADIÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                add = n1 + n2
                palpite = int(
                    input(f"Se somarmos \033[1;31m{n1}\033[m com \033[1;31m{n2}\033[m qual o resultado?\nDigite: "))
                if add == palpite:
                    acertos += 1
                    print(f"\033[1;34m{add}!\033[m Certa resposta! Parabéns \033[4;31m{nome}!\033[m")
                else:
                    print(f"Ops, errou ):\nVamos lá \033[4;31m{nome}\033[m, concentre-se mais e tente novamente!")
                    erros += 1

            elif sorteio_operacao == "-":
                n1 = randint(0, 100)
                n2 = randint(0, 100)

                while True:
                    if n1 >= n2:
                        sorteados = [n1, n2]
                        break
                    else:
                        n1 = randint(0, 100)
                        n2 = randint(0, 100)
                print(f"Escolhi \033[1;35mSUBTRAÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                sub = n1 - n2
                palpite = int(
                    input(f"\033[1;31m{n1}\033[m menos \033[1;31m{n2}\033[m, é?\nDigite: "))
                if sub == palpite:
                    acertos += 1
                    print(f"\033[1;34m{sub}!\033[m Muito bem, \033[4;31m{nome}!\033[m Certa resposta!")
                else:
                    print(f"\033[4;31m{nome}\033[m, dessa vez você errou ):\nMas sei que na próxima você vai acertar!")
                    erros += 1

            elif sorteio_operacao == "*":
                n1 = randint(0, 100)
                n2 = randint(0, 10)
                print(f"Escolhi \033[1;35mMULTIPLICAÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                mult = n1 * n2
                palpite = int(input(
                    f"Se multiplicarmos \033[1;31m{n1}\033[m por \033[1;31m{n2}\033[m, qual o resultado?\nDigite: "))
                if mult == palpite:
                    acertos += 1
                    print(f"\033[1;34m{mult}!\033[m Correto, \033[4;31m{nome}!!\033[m")
                else:
                    print(f"Não foi dessa vez \033[4;31m{nome}\033[m ):\nQuem sabe na próxima!?")
                    erros += 1

            elif sorteio_operacao == "/":
                n1 = randint(1, 100)
                n2 = randint(1, 10)
                while True:
                    if n1 >= n2:
                        sorteados = [n1, n2]
                        break
                    else:
                        n1 = randint(1, 100)
                        n2 = randint(1, 10)
                print(
                    f"Escolhi \033[1;35mDIVISÃO\033[m para te desafiar "
                    f"e você vai me dizer qual o valor da \033[4;35mDIVISÃO INTEIRA\033[m, e o \033[4;35mRESTO\033[m da divisão, tá bom?!")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                div = n1 // n2
                resto = n1 % n2
                palpite_div = int(input(f"A DIVISÃO INTEIRA de \033[1;31m{n1}\033[m por \033[1;31m{n2}\033[m é...?\nDigite: "))
                palpite_resto = int(input(f"O RESTO da divisão de \033[1;31m{n1}\033[m por \033[1;31m{n2}\033[m é...?\nDigite: "))
                if palpite_div == div and palpite_resto == resto:
                    acertos += 1
                    print(f"\033[1;34m{div}\033[m divisão inteira e \033[1;34m{resto}\033[m resto da divisão.\nPerfeito \033[4;31m{nome}!!\033[m")
                else:
                    print(f"ERROU!\n\033[4;31m{nome}\033[m, vamos lá, na próxima se concentre mais!")
                    erros += 1

        print(
            f"\nVocê jogou {rodada} vezes e obteve \033[1;34m{acertos}\033[m acerto(s) e \033[1;34m{erros}\033[m erro(s).\n")
        if acertos == 5:
            print("EXCELENTE! Você acertou tudo!\n\033[3;33mNota A!!\033[m\n")
        elif acertos == 4:
            print("Muito bom! Por pouco não acertou tudo!\n\033[3;32mNota B!!\033[m\n")
        elif acertos == 3:
            print("Ficou na média... Quem sabe não melhora na próxima?\n\033[3;34mNota C!!\033[m\n")
        elif acertos == 2:
            print("2 acertos não é bom hein... :/\n\033[3;35mNota D!!\033[m\n")
        else:
            print(
                "Acho que você precisa estudar mais matemática!!\n\033[1;31mNota E!!\033\n[m")

        escolha_sim = input(f"Deseja jogar de novo? (S = sim /N = não)").upper()

        if escolha_sim == "S":
            rodada = 0
            print("\033[1;33mLegal, vamos lá!!\033[m")
            continue
        else:
            print(f"Obrigado por jogar, \033[4;31m{nome}!\033[m Precisando treinar matemática, só chamar!")
            break

def nivel_Dificil():
    nome = str(input("\033[1;35mDigite seu nome: \033[m").upper())
    if nome == "HELENA":
        print(f"\033[4;31m{nome}!\033[m Que nome bonito, né?! :)\n")
        sleep(1.5)
    else:
        print(f"Prazer \033[4;31m{nome}!\033[m\n")
        sleep(1.5)

    input("\033[4;35mVocê gosta de adição e subtração? Prefere divisão ou multiplicação?\n"
          "Vou sortear DOIS números pra você e depois a operação matemática para o cálculo.\033[m\033[1;37m>>Enter\033[m")
    input('\n\033[4;35mVocê terá 5 rodadas e no final, terá sua nota. Vamos ver se está em dia com o raciocínio?\n'
          'E tenha atenção, pois você agora está no nível difícil.\033[m\033[1;37m>>Enter\033[m')
    sleep(1.5)

    # ESCOLHA RANDOMICA DE OPERACAO E NUMEROS
    again = True
    while again:

        rodada = 0
        acertos = 0
        erros = 0
        while rodada <= 4:
            rodada += 1

            print(f"\n\033[1;30;45mRODADA {rodada}\033[m\n")
            sleep(1)
            op = ["+", "-", "*", "/"]
            sorteio_operacao = choice(op)

            if sorteio_operacao == "+":
                n1 = randint(0, 1000)
                n2 = randint(0, 1000)
                print("Escolhi \033[1;35mADIÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                add = n1 + n2
                palpite = int(
                    input(f"Se somarmos \033[1;31m{n1}\033[m com \033[1;31m{n2}\033[m qual o resultado?\nDigite: "))
                if add == palpite:
                    acertos += 1
                    print(f"\033[1;34m{add}!\033[m Certa resposta! Parabéns \033[4;31m{nome}!\033[m")
                else:
                    print(f"Ops, errou ):\nVamos lá \033[4;31m{nome}\033[m, concentre-se mais e tente novamente!")
                    erros += 1

            elif sorteio_operacao == "-":
                n1 = randint(0, 1000)
                n2 = randint(0, 1000)
                print(f"Escolhi \033[1;35mSUBTRAÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                sub = n1 - n2
                palpite = int(
                    input(f"\033[1;31m{n1}\033[m menos \033[1;31m{n2}\033[m, é?\nDigite: "))
                if sub == palpite:
                    acertos += 1
                    print(f"\033[1;34m{sub}!\033[m Muito bem, \033[4;31m{nome}!\033[m Certa resposta!")
                else:
                    print(f"\033[4;31m{nome}\033[m, dessa vez você errou ):\nMas sei que na próxima você vai acertar!")
                    erros += 1

            elif sorteio_operacao == "*":
                n1 = randint(0, 1000)
                n2 = randint(0, 100)
                print(f"Escolhi \033[1;35mMULTIPLICAÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                mult = n1 * n2
                palpite = int(input(
                    f"Se multiplicarmos \033[1;31m{n1}\033[m por \033[1;31m{n2}\033[m, qual o resultado?\nDigite :"))
                if mult == palpite:
                    acertos += 1
                    print(f"\033[1;34m{mult}!\033[m Correto, \033[4;31m{nome}!!\033[m")
                else:
                    print(f"Não foi dessa vez \033[4;31m{nome}\033[m ):\nQuem sabe na próxima!?")
                    erros += 1

            elif sorteio_operacao == "/":
                n1 = randint(1, 1000)
                n2 = randint(1, 100)
                while True:
                    if n1 >= n2:
                        sorteados = [n1, n2]
                        break
                    else:
                        n1 = randint(1, 1000)
                        n2 = randint(1, 100)

                print("Escolhi \033[1;35mDIVISÃO\033[m para te desafiar!\nLembre-se da regra de arredondamentos de números.")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                div = n1 / n2
                div = round(div, 1)
                palpite = float(f"A divisão de \033[1;31m{n1}\033[m por \033[1;31m{n2}\033[m é...?\n"
                          f"Digite (Digite apenas UM número decimal se precisar (exemplo: XXX.X): ")
                palpite = round(palpite, 1)
                if div == palpite:
                    acertos += 1
                    print(f"\033[1;34m{div:.1f}!\033[m Perfeito \033[4;31m{nome}!!\033[m")
                else:
                    print(f"ERROU!\n\033[4;31m{nome}\033[m, vamos lá, na próxima se concentre mais!")
                    erros += 1

        print(
            f"\nVocê jogou {rodada} vezes e obteve \033[1;34m{acertos}\033[m acerto(s) e \033[1;34m{erros}\033[m erro(s).\n")
        if acertos == 5:
            print("EXCELENTE! Você acertou tudo!\n\033[3;33mNota A!!\033[m\n")
        elif acertos == 4:
            print("Muito bom! Por pouco não acertou tudo!\n\033[3;32mNota B!!\033[m\n")
        elif acertos == 3:
            print("Ficou na média... Quem sabe não melhora na próxima?\n\033[3;34mNota C!!\033[m\n")
        elif acertos == 2:
            print("2 acertos não é bom hein... :/\n\033[3;35mNota D!!\033[m\n")
        else:
            print(
                "Acho que você precisa estudar mais matemática!!\n\033[1;31mNota E!!\033\n[m")

        escolha_sim = input(f"Deseja jogar de novo? (S = sim /N = não)").upper()

        if escolha_sim == "S":
            rodada = 0
            print("\033[1;33mLegal, vamos lá!!\033[m")
            continue
        else:
            print(f"Obrigado por jogar, \033[4;31m{nome}!\033[m Precisando treinar matemática, só chamar!")
            break

def nivel_SuperHard():
    nome = str(input("\033[1;35mDigite seu nome: \033[m").upper())
    if nome == "HELENA":
        print(f"\033[4;31m{nome}!\033[m Que nome bonito, né?! :)\n")
        sleep(1.5)
    else:
        print(f"Prazer \033[4;31m{nome}!\033[m\n")
        sleep(2)

    input("\033[4;35mVocê gosta de adição e subtração? Prefere divisão ou multiplicação?\n"
          "Vou sortear DOIS números pra você e depois a operação matemática para o cálculo.\033[m\033[1;37m>>Enter\033[m")
    input('\n\033[4;35mSe você domina matemática, saberá a resposta!\nVocê terá 5 rodadas e no final, terá sua nota.\n'
          'Vamos ver se está em dia com o raciocínio? E agora, você está no nível SUPER DIFICIL.\n'
          'Atenção e conhecimento matemático são imprescindíveis aqui!\033[m\033[1;37m>>Enter\033[m')
    sleep(2)

    # ESCOLHA RANDOMICA DE OPERACAO E NUMEROS
    again = True
    while again:

        rodada = 0
        acertos = 0
        erros = 0
        while rodada <= 4:
            rodada += 1

            print(f"\n\033[1;30;45mRODADA {rodada}\033[m\n")
            sleep(1)
            op = ["+", "-", "*", "/"]
            sorteio_operacao = choice(op)

            if sorteio_operacao == "+":
                n1 = randint(0, 1000)
                n2 = randint(0, 1000)
                print("Escolhi \033[1;35mADIÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                add = n1 + n2
                palpite = int(
                    input(f"Se somarmos \033[1;31m{n1}\033[m com \033[1;31m{n2}\033[m qual o resultado?\nDigite: "))
                if add == palpite:
                    acertos += 1
                    print(f"\033[1;34m{add}!\033[m Certa resposta! Parabéns \033[4;31m{nome}!\033[m")
                else:
                    print(f"Ops, errou ):\nVamos lá \033[4;31m{nome}\033[m, concentre-se mais e tente novamente!")
                    erros += 1

            elif sorteio_operacao == "-":
                n1 = randint(0, 1000)
                n2 = randint(0, 1000)
                print(f"Escolhi \033[1;35mSUBTRAÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                sub = n1 - n2
                palpite = int(
                    input(f"\033[1;31m{n1}\033[m menos \033[1;31m{n2}\033[m, é?\nDigite: "))
                if sub == palpite:
                    acertos += 1
                    print(f"\033[1;34m{sub}!\033[m Muito bem, \033[4;31m{nome}!\033[m Certa resposta!")
                else:
                    print(f"\033[4;31m{nome}\033[m, dessa vez você errou ):\nMas sei que na próxima você vai acertar!")
                    erros += 1

            elif sorteio_operacao == "*":
                n1 = randint(0, 1000)
                n2 = randint(0, 1000)
                print(f"Escolhi \033[1;35mMULTIPLICAÇÃO\033[m para te desafiar")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                mult = n1 * n2
                palpite = int(input(
                    f"Se multiplicarmos \033[1;31m{n1}\033[m por \033[1;31m{n2}\033[m, qual o resultado?\nDigite :"))
                if mult == palpite:
                    acertos += 1
                    print(f"\033[1;34m{mult}!\033[m Correto, \033[4;31m{nome}!!\033[m")
                else:
                    print(f"Não foi dessa vez \033[4;31m{nome}\033[m ):\nQuem sabe na próxima!?")
                    erros += 1

            elif sorteio_operacao == "/":
                n1 = randint(1, 1000)
                n2 = randint(1, 100)
                print("Escolhi \033[1;35mDIVISÃO\033[m para te desafiar!\nLembre-se da regra de arredondamento de números")
                print("\033[1;37mSorteando os números...\033[m")
                sleep(2)
                print(f"\nO primeiro número sorteado foi \033[1;31m{n1}\033[m")
                sleep(1.5)
                print(f"O segundo número sorteado foi \033[1;31m{n2}\033[m\n")
                div = n1 / n2
                div = round(div, 2)
                palpite = float(
                    input(
                        f"A divisão de \033[1;31m{n1}\033[m por \033[1;31m{n2}\033[m é...?\nDigite "
                        f"(Digite apenas UM número decimal se precisar (exemplo: XXXX.XX): "))
                palpite = round(palpite, 2)
                if div == palpite:
                    acertos += 1
                    print(f"\033[1;34m{div:.2f}!\033[m Perfeito \033[4;31m{nome}!!\033[m")
                else:
                    print(f"ERROU!\n\033[4;31m{nome}\033[m, vamos lá, na próxima se concentre mais!")
                    erros += 1

        print(
            f"\nVocê jogou {rodada} vezes e obteve \033[1;34m{acertos}\033[m acerto(s) e \033[1;34m{erros}\033[m erro(s).\n")
        if acertos == 5:
            print("EXCELENTE! Você acertou tudo!\n\033[3;33mNota A!!\033[m\n")
        elif acertos == 4:
            print("Muito bom! Por pouco não acertou tudo!\n\033[3;32mNota B!!\033[m\n")
        elif acertos == 3:
            print("Ficou na média... Quem sabe não melhora na próxima?\n\033[3;34mNota C!!\033[m\n")
        elif acertos == 2:
            print("2 acertos não é bom hein... :/\n\033[3;35mNota D!!\033[m\n")
        else:
            print(
                "Acho que você precisa estudar mais matemática!!\n\033[1;31mNota E!!\033\n[m")

        escolha_sim = input(f"Deseja jogar de novo? (S = sim /N = não)").upper()

        if escolha_sim == "S":
            rodada = 0
            print("\033[1;33mLegal, vamos lá!!\033[m")
            continue
        else:
            print(f"Obrigado por jogar, \033[4;31m{nome}!\033[m Precisando treinar matemática, só chamar!")
            break

#INICIO

inicio()