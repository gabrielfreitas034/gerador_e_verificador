def converter_temperatura():
    try:
        print("\033[1;33mEscolha a conversão:\033[m")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        escolha = int(input("\033[1;32mDigite sua escolha (1 ou 2):\033[m ").strip())

        if escolha == 1:
            celsius = float(input("\033[1;33mDigite a temperatura em Celsius:\033[m ").strip())
            fahrenheit = (celsius * 9/5) + 32
            print(f"\033[1;32m{celsius}°C é igual a {fahrenheit:.2f}°F\033[m")
        elif escolha == 2:
            fahrenheit = float(input("\033[1;33mDigite a temperatura em Fahrenheit:\033[m ").strip())
            celsius = (fahrenheit - 32) * 5/9
            print(f"\033[1;32m{fahrenheit}°F é igual a {celsius:.2f}°C\033[m")
        else:
            print("\033[1;31mEscolha inválida. Tente novamente.\033[m")
    except ValueError:
        print("\033[1;31mErro: Certifique-se de digitar apenas números válidos.\033[m")
