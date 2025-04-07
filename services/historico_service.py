from utils.terminal_utils import limpar_tela, exibir_mensagem

def exibir_historico(historico):
    limpar_tela()
    print("\033[1;34m")  # Cor azul brilhante
    print("=" * 50)
    print("{:^50}".format("HISTÓRICO DE OPERAÇÕES"))
    print("=" * 50)
    if not historico:
        print("\033[1;31mNenhuma operação realizada até o momento.\033[m")
    else:
        for i, operacao in enumerate(historico, 1):
            print(f"{i}. {operacao}")
    print("\033[m")
    input("\033[1;33mPressione Enter para voltar ao menu principal...\033[m")

def exportar_resultados(historico):
    limpar_tela()
    try:
        with open("resultados.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("HISTÓRICO DE OPERAÇÕES\n")
            arquivo.write("=" * 50 + "\n")
            if not historico:
                arquivo.write("Nenhuma operação realizada até o momento.\n")
            else:
                for operacao in historico:
                    arquivo.write(f"{operacao}\n")
        exibir_mensagem("\033[1;32mResultados exportados com sucesso para 'resultados.txt'.\033[m", cor="verde")
    except Exception as e:
        exibir_mensagem(f"\033[1;31mErro ao exportar resultados: {str(e)}\033[m", cor="vermelho")

def exibir_ajuda_historico():
    limpar_tela()
    print("\033[1;34m")  # Cor azul brilhante
    print("=" * 50)
    print("{:^50}".format("AJUDA - HISTÓRICO"))
    print("=" * 50)
    print("\033[1;37m1. Exibir Histórico: Mostra todas as operações realizadas durante a execução do programa.")
    print("2. Exportar Resultados: Salva o histórico de operações em um arquivo de texto chamado 'resultados.txt'.")
    print("\033[m")
    input("\033[1;33mPressione Enter para voltar ao menu principal...\033[m")
