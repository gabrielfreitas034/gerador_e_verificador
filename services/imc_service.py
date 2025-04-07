def calcular_imc():
    try:
        peso = float(input("\033[1;33mDigite seu peso (kg):\033[m ").strip())
        altura = float(input("\033[1;33mDigite sua altura (m):\033[m ").strip())
        imc = peso / (altura ** 2)
        print(f"\033[1;32mSeu IMC é: {imc:.2f}\033[m")
        if imc < 18.5:
            print("\033[1;34mClassificação: Abaixo do peso\033[m")
        elif 18.5 <= imc < 24.9:
            print("\033[1;32mClassificação: Peso normal\033[m")
        elif 25 <= imc < 29.9:
            print("\033[1;33mClassificação: Sobrepeso\033[m")
        else:
            print("\033[1;31mClassificação: Obesidade\033[m")
    except ValueError:
        print("\033[1;31mErro: Certifique-se de digitar apenas números válidos.\033[m")
