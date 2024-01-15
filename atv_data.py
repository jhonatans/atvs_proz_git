import datetime


def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade


def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(
                input("Digite o ano de nascimento (1922 a 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano de nascimento fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um ano válido.")


def main():
    nome_completo = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()

    idade = calcular_idade(ano_nascimento)

    print(f"\nNome: {nome_completo}")
    print(f"Idade em 2022: {idade} anos")


if __name__ == "__main__":
    main()
