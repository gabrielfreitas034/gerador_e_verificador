from funcoes_menu import *

while True: 
    limpar_tela()
    menu_opcoes()
    escolha =  obter_escolha()

    if escolha == 1:
        print('\n\033[35mCPF GERADO:' ,gerar_cpf())

    elif escolha == 2 :
        print(verifica_cpf())

    elif escolha == 3:
        print(gerar_senha())

    else:
        print('\033[31mDIGITE AS OPÇÕES VÁLIDAS\033[m')
        tempo()
        continue

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\n\033[33mDeseja escolher outra opção? [S/N]\033[m  ')).strip().upper()[0]
        limpar_tela()

    if continuar == 'N': 
        print(f'\n\033[33mPROGRAMA FECHADO!\033[m')
        break
    
    