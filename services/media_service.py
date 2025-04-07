def calcular_media():
    try:
        numeros = input("\033[1;33mDigite os números separados por vírgula:\033[m ").strip()
        lista_numeros = [float(num) for num in numeros.split(",")]
        media = sum(lista_numeros) / len(lista_numeros)
        print(f"\033[1;32mA média é: {media:.2f}\033[m")
    except ValueError:
        print("\033[1;31mErro: Certifique-se de digitar apenas números válidos.\033[m")
