# -*- coding: utf-8 -*-
from turtle import *
import time
import perguntas
from random import randint

def get_nome_pergunta():
    nome = []
    file = open('perguntas.py')
    for linha in file:
        if 'def' in linha:
            nome.append(linha.split()[1].split("(")[0])
    return nome


def main():
    """
    Comentário do método main

    """
    rand = randint(0, len(get_nome_pergunta()))
    Pergunta = getattr(perguntas, 'p'+str(rand))

    if Pergunta():
        goto(-320, -215)
    else:
        goto(-320, -215)
        break

    # bgpic("resource/mapa.gif")
    #
    # shape("turtle")
    #
    # fillcolor("purple")
    #
    # turtlesize(2)
    #
    # penup()
    # # bolinha 01
    # time.sleep(10)
    #
    # goto(-320, -215)
    #
    # # bolinha 02
    # goto(-90, -225)
    #
    # # bolinha 03
    # goto(140, -230)
    #
    # # bolinha 04
    # goto(325, -135)
    #
    # # bolinha 05
    # goto(310, 110)
    #
    # # bolinha 06
    # goto(125, 230)
    #
    # # bolinha 07
    # goto(-120, 220)
    #
    # # bolinha 08
    # goto(-330, 300)

if __name__ == "__main__":
    main()



