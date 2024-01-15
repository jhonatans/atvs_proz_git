def calculadora():
    while True:
        print("\nOperações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        try:
            escolha = int(input("Digite o número para a operação desejada: "))

            if escolha == 0:
                print("Saindo da calculadora.")
                break

            if escolha < 1 or escolha > 4:
                print("Essa opção não existe. Tente novamente.")
                continue

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == 4 and num2 == 0:
                print("Erro: Divisão por zero. Tente novamente.")
                continue

            resultado = realizar_operacao(num1, num2, escolha)
            print(f"Resultado: {resultado}")

        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def realizar_operacao(num1, num2, escolha):
    if escolha == 1:
        return num1 + num2
    elif escolha == 2:
        return num1 - num2
    elif escolha == 3:
        return num1 * num2
    elif escolha == 4:
        return num1 / num2


calculadora()
