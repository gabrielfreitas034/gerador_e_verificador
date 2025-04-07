from random import sample
from utils.terminal_utils import tempo, exibir_mensagem

def gerar_senha():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&-_*()!"
    senha = ''.join(sample(caracteres, 10))
    tempo()
    return senha
