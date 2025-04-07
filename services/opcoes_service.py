from services.cpf_service import gerar_cpf, verifica_cpf
from services.password_service import gerar_senha
from services.media_service import calcular_media
from services.temperatura_service import converter_temperatura
from services.imc_service import calcular_imc
from utils.terminal_utils import exibir_mensagem, tempo

def executar_opcao(escolha):
    try:
        print("\n\033[1;34m" + "-" * 40 + "\033[m")  # Linha azul brilhante
        if escolha == 1:
            cpf = gerar_cpf()
            exibir_mensagem(f"CPF GERADO: \033[1;32m{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\033[m", cor="ciano")
            return f"CPF Gerado: {cpf}"
        elif escolha == 2:
            resultado = verifica_cpf()
            exibir_mensagem(resultado, cor="verde")
            return f"Verificação de CPF: {resultado}"
        elif escolha == 3:
            senha = gerar_senha()
            exibir_mensagem(f"SENHA GERADA: \033[1;36m{senha}\033[m", cor="roxo")
            return f"Senha Gerada: {senha}"
        elif escolha == 4:
            calcular_media()
            return "Média calculada com sucesso."
        elif escolha == 5:
            converter_temperatura()
            return "Temperatura convertida com sucesso."
        elif escolha == 6:
            calcular_imc()
            return "IMC calculado com sucesso."
        else:
            exibir_mensagem("\033[1;31mDIGITE UMA OPÇÃO VÁLIDA\033[m", cor="vermelho")
            tempo()
            return "Opção inválida."
        print("\033[1;34m" + "-" * 40 + "\033[m")  # Linha azul brilhante
    except Exception as e:
        exibir_mensagem(f"\033[1;31mERRO: {str(e)}\033[m", cor="vermelho")
        return f"Erro: {str(e)}"
