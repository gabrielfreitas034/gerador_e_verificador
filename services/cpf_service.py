from random import randint
from utils.terminal_utils import tempo, exibir_mensagem

def gerar_cpf():
    cpf_9_digitos = ''.join([str(randint(0, 9)) for _ in range(9)])
    digito_1 = calcular_digito(cpf_9_digitos, 10)
    cpf_10_digitos = cpf_9_digitos + str(digito_1)
    digito_2 = calcular_digito(cpf_10_digitos, 11)
    cpf_completo = cpf_10_digitos + str(digito_2)
    tempo()
    return cpf_completo

def verifica_cpf():
    cpf = input("\033[35mDigite seu CPF (com ou sem pontuação):\033[m ").replace('.', '').replace('-', '').strip()
    if len(cpf) != 11 or not cpf.isdigit():
        return "\033[31mCPF inválido\033[m"

    if not validar_digito(cpf, 9, 10) or not validar_digito(cpf, 10, 11):
        return "\033[31mCPF inválido\033[m"

    return f"\033[32mCPF válido: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\033[m"

def calcular_digito(cpf, peso):
    soma = sum(int(digito) * peso for digito, peso in zip(cpf, range(peso, 1, -1)))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_digito(cpf, tamanho, peso):
    soma = sum(int(cpf[i]) * (peso - i) for i in range(tamanho))
    resto = soma % 11
    digito = 0 if resto < 2 else 11 - resto
    return str(digito) == cpf[tamanho]
