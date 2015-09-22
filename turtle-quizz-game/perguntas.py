# -*- coding: utf-8 -*-
import time
import sys
from random import *


cabecalho = """
            ** Apenas uma das alternativas está correta.      **
            ** As opções validas para input sao : a, b, c, d  **
            """

def validacao_input(resposta):
    """
    Verfica se a resposta esta entre as opções validas
    retorna True ou False
    """
    opcoes_validas = ["a","b","c","d"]
    return True if resposta not in opcoes_validas else False
    


def pergunta1():
    """
    Função que representa a pergunta, armazena o enunciado e a resposta correta
    retorna True ou False
    """    
    enunciado = cabecalho + """
                Como as enzimas se reproduzem?

                a) Fica uma enzima da outra
                b) Nao se reproduzem
                c) Reproduzem por osmose
                d) Nenhuma das alternativas

                """
    _resp_correta = "a" 

    #Input dentro de um laço de validação, só sai se estiver validado
    flag = True;
    while flag:
        resposta = raw_input(enunciado)
        flag = validacao_input(resposta)

    return(True if resposta == _resp_correta else False)


def pergunta2():
    """
    Função que representa a pergunta, armazena o enunciado e a resposta correta
    retorna True ou False
    """    
    enunciado = cabecalho + """
                Qual é o nome da captal da africa?

                a) Zimbaboe
                b) Angola
                c) Jafers Baey
                d) Moçambique

                """
    _resp_correta = "b" 


    #Input dentro de um laço de validação, só sai se estiver validado
    flag = True;
    while flag:
        resposta = raw_input(enunciado)
        flag = validacao_input(resposta)

    return(True if resposta == _resp_correta else False)




