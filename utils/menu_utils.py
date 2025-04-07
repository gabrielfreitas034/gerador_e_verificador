from utils.terminal_utils import limpar_tela

def exibir_cabecalho():
    print("\033[1;36m")  # Cor ciano brilhante
    print("=" * 50)
    print("\033[1;32m{:^50}".format("MENU PRINCIPAL"))  # Texto centralizado em verde brilhante
    print("\033[1;36m" + "=" * 50 + "\033[m")  # Cor ciano brilhante e reset

def exibir_menu():
    print("\033[1;33m")  # Cor amarela brilhante
    print("0. Sair do Programa")
    print("1. Gerar CPF")
    print("2. Verificar CPF")
    print("3. Gerar Senha")
    print("4. Calcular Média")
    print("5. Converter Temperatura")
    print("6. Calcular IMC")
    print("7. Exibir Histórico")
    print("8. Exportar Resultados")
    print("9. Ajuda")
    print("\033[1;33m" + "-" * 50 + "\033[m")  # Linha amarela brilhante
    print("\033[1;32mESCOLHA UMA OPÇÃO:\033[m")  # Texto em verde brilhante

def exibir_ajuda():
    limpar_tela()
    print("\033[1;34m")  # Cor azul brilhante
    print("=" * 50)
    print("{:^50}".format("AJUDA"))
    print("=" * 50)
    print("\033[1;37m1. Gerar CPF: Gera um CPF válido aleatório.")
    print("2. Verificar CPF: Verifica se um CPF fornecido é válido.")
    print("3. Gerar Senha: Cria uma senha segura aleatória.")
    print("4. Calcular Média: Calcula a média de uma lista de números.")
    print("5. Converter Temperatura: Converte entre Celsius e Fahrenheit.")
    print("6. Calcular IMC: Calcula o Índice de Massa Corporal.")
    print("7. Exibir Histórico: Mostra o histórico de operações realizadas.")
    print("8. Exportar Resultados: Exporta o histórico para um arquivo.")
    print("9. Ajuda: Exibe este menu de ajuda.")
    print("\033[m")
    input("\033[1;33mPressione qualquer tecla para voltar ao menu principal...\033[m")

def obter_escolha():
    try:
        return int(input("\033[1;32mDigite sua escolha: \033[m").strip())
    except ValueError:
        raise ValueError("Entrada inválida! Por favor, insira um número.")
