# -*- coding: utf-8 -*-
from turtle import *
import time
import perguntas
from random import randint

def get_nome_pergunta():
    """
    Abre o arquivo de perguntas, pega os nomes das funções e retorna em uma lista
    """
    nome = []
    file = open('perguntas.py')
    [nome.append(linha.split()[1].split("(")[0]) if 'def' in linha else linha for linha in file]
    file.close()
    return nome


def main():
    """
    Carrega o tabuleiro, carrega as configurações iniciais, analisa as jogadas e apresenta os resultados.
    """
    #incializando o tabuleiro e definindo a tartaruga
    bgpic("resource/mapa.gif")
    shape("turtle")
    fillcolor("purple")
    turtlesize(3)
    penup()

    #configuração inicial do jogo
    x = y = -250
    erro = acerto = 0
    rodando = True
    max_tentativas = 10
    
    #coloca a tartaruga na posicao incial e chama as perguntas
    goto(x, y)
    while rodando:
        Pergunta = getattr(perguntas, 'pergunta'+str(randint(1, len(get_nome_pergunta())-1)));
        if Pergunta():
            x += 100; y += 100; acerto += 1
        else:
            y = x = -220; erro += 1
        goto(x, y);
        print("quantidade de jogadas ate agora = %s\ncertas = %s\nerradas = %s\n" % (acerto+erro, acerto, erro))
        rodando = False if acerto+erro == max_tentativas else rodando
    
    #finalizando o jogo, apresentação de pontos e opção de reinicio
    print("Voce atingiu a quantidade maxima de %s jogadas \n%s certas \n%s erradas\n" % (max_tentativas, acerto, erro)) 
    op = raw_input(u'Gostaria de jogar novamente? |sim|nao|: ')
    if op == 'sim': main()
    
if __name__ == "__main__": 
    main()



