from utils.menu_utils import exibir_menu, exibir_cabecalho, exibir_ajuda, obter_escolha
from services.opcoes_service import executar_opcao
from services.historico_service import exibir_historico, exportar_resultados
from utils.terminal_utils import limpar_tela, exibir_mensagem

historico = []  # Lista para armazenar o histórico de operações

def main():
    while True:
        try:
            limpar_tela()
            exibir_cabecalho()
            exibir_menu()
            escolha = obter_escolha()

            if escolha == 0:  # Sair do programa
                exibir_mensagem("\033[1;31mPROGRAMA FECHADO!\033[m", cor="amarelo")
                break
            elif escolha == 9:  # Ajuda
                exibir_ajuda()
            elif escolha == 7:  # Exibir histórico
                exibir_historico(historico)
                input("\033[1;33mPressione Enter para voltar ao menu principal...\033[m")
            elif escolha == 8:  # Exportar resultados
                exportar_resultados(historico)
                input("\033[1;33mPressione qualquer tecla para voltar ao menu principal...\033[m")
            elif 1 <= escolha <= 6:
                resultado = executar_opcao(escolha)
                historico.append(f"Opção {escolha}: {resultado}" if resultado else f"Opção {escolha}: Operação concluída sem retorno.")
            else:
                exibir_mensagem("\033[1;31mOpção inválida! Tente novamente.\033[m", cor="vermelho")

            while True:
                continuar = input('\n\033[1;33mDeseja escolher outra opção? [S/N]\033[m ').strip().upper()
                if continuar in ['S', 'N']:
                    break
                exibir_mensagem("\033[1;31mOpção inválida! Digite apenas 'S' ou 'N'.\033[m", cor="vermelho")

            if continuar == 'N':
                exibir_mensagem("\033[1;31mPROGRAMA FECHADO!\033[m", cor="amarelo")
                break
        except ValueError:
            exibir_mensagem("\033[1;31mEntrada inválida! Por favor, insira um número.\033[m", cor="vermelho")
        except Exception as e:
            exibir_mensagem(f"\033[1;31mERRO FATAL: {str(e)}\033[m", cor="vermelho")
            break

if __name__ == "__main__":
    main()
