from random import randint, sample
import os ,time

# Gerador de cpf 
def gerar_cpf():
    cpf_9_digitos = ''
    for i in range(9):
        cpf_9_digitos += str(randint(0,9))

    contagem_regressiva_10 = 10
    resto_1 = 0
    for digito in cpf_9_digitos:
        resto_1 += int(digito) * contagem_regressiva_10
        contagem_regressiva_10 -= 1
    digito_1 = resto_1 % 11
    if digito_1 < 2:
        digito_1 == 0
    else:
        digito_1 = 11 - digito_1

    cpf_10_digitos = cpf_9_digitos + str(digito_1)

    contagem_regressiva_11 = 11 
    resto_2  = 0
    for digito in cpf_10_digitos:
        resto_2 += int(digito) * contagem_regressiva_11
        contagem_regressiva_11 -= 1
    digito_2 = resto_2 % 11
    if digito_2 < 2:
        digito_2 == 0
    else:
        digito_2 = 11 - digito_2

    cpf_completo = cpf_10_digitos + str(digito_2)
    gerando()
    tempo()
    return f'\033[36m{cpf_completo}\033[m'

# Verificador de CPF
def verifica_cpf():
    cpf = input(f'\n\033[35mDigite seu CPF:(APENAS DIGITOS)\033[m\033[36m\033[m ')

    # verifica se tem 11 digitos 
    if len(cpf) != 11:
        tempo()
        verificando()
        return '\033[31mCPF inválido\033[m'

    # verifica 10º digíto
    contador_10 = 10
    soma_10 = 0
    for i in range(9):
        soma_10 += contador_10 * int(cpf[i])
        contador_10 -= 1
    resto_10 = soma_10 % 11
    if resto_10 < 2:
        resto_10 = 0
    else:
        resto_10 = 11 - resto_10 

    if str(resto_10) != cpf[9]:
        tempo()
        verificando()
        return '\033[31mCPF inválido\033[m'
    
    # verifica 11º digíto
    contador_11 = 11
    soma_11 = 0
    for i in range(10):
        soma_11 += contador_11 * int(cpf[i])
        contador_11 -= 1
    resto_11 = soma_11 % 11
    if resto_11 < 2:
        resto_11 = 0
    else:
        resto_11 = 11 - resto_11    
    
    if str(resto_11) != cpf[10]:
        tempo()
        verificando()
        return '\033[31mCPF inválido\033[m'

    tempo()
    verificando()  
    return '\033[32mCPF válido\033[m'

# Gerado de senhas
def gerar_senha():
    lower_case = ('abcdefghijklmnopqrstuvwxyz')
    uppers_case = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = ('0123456789')
    symbols = ('@#$%^&-_*()!')
    for_pass = lower_case + uppers_case + numbers + symbols
    len_password = 10
    password = ''.join(sample(for_pass, len_password))

    gerando()
    tempo()
    return f'\n\033[35mSENHA GERADA:\033[m \033[36m{password}'  

# Menu opções
def menu_opcoes():
    print ('''\033[33mOPÇÕES:
    [1] GERAR CPF
    [2] VERIFICAR CPF 
    [3] GERAR SENHA''')

# obter escolha
def obter_escolha():
    while True:
        try:
            escolha = int(input('\n\033[33mQUAL SUA ESCOLHA?\033[m '))
            return escolha
        except ValueError:
            limpar_tela()
            tempo()
            print('\033[31mDIGITE AS OPÇÕES VÁLIDAS\033[m\n')
            menu_opcoes()


# Limpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Print Gerando
def gerando():
    print('\nGERANDO...')

# Print Verificando
def verificando():
    print('\nVERIFICANDO...')

# Tempo de espera
def tempo():
    time.sleep(1)
