import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_mensagem(mensagem, cor="branco"):
    cores = {
        "branco": "\033[m",
        "vermelho": "\033[31m",
        "amarelo": "\033[33m",
        "verde": "\033[32m",
        "azul": "\033[34m",
        "roxo": "\033[35m",
        "ciano": "\033[36m",
    }
    print(f"{cores.get(cor, 'branco')}{mensagem}\033[m")

def tempo(segundos=1):
    time.sleep(segundos)
