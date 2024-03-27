import time
import os


def entradaDados(limpaTela):
    # Entrada do valor do veiculo
    while True:
        try:
            valor = float(input("Digite o valor do carro: "))
            if isinstance(valor, float):
                break

        except ValueError:
            print("Erro: Você deve digitar um valor real!")
            time.sleep(1.5)
            os.system(limpaTela)
            print("========= .:| Inclusão de veículo |:. ========= ")

    # Entrada do modelo do veiculo
    while True:
        try:
            modelo = input("Digite o modelo do carro: ")
            if modelo[0].isdigit():
                raise ValueError(
                    "O primeiro caractere do nome do veículo não pode ser numérico!"
                )
            else:
                break
        except ValueError as e:
            print(e)
            time.sleep(1.8)
            os.system(limpaTela)
            print("========= .:| Inclusão de veículo |:. ========= ")
            print(f"Digite o valor do carro: {valor}")

    # Entrada da cor do veiculo
    while True:
        try:
            cor = input("Digite a cor do carro: ")
            flag = False
            for caractere in cor:
                if caractere.isdigit():
                    flag = True
                    break
            if flag == True:
                raise ValueError("A cor não deve ter caracteres numéricos!")
            else:
                break
        except ValueError as e:
            print(e)
            time.sleep(1.8)
            os.system(limpaTela)
            print("========= .:| Inclusão de veículo |:. ========= ")
            print(f"Digite o valor do carro: {valor}")
            print(f"Digite o modelo do carro: {modelo}")


# Entrada da quilometragem do veiculo
    while True:
        try:
            quilometragem = int(input("Digite a quilometragem do carro: "))
            if isinstance(quilometragem, int):
                break

        except ValueError:
            print("Erro: Você deve digitar um valor inteiro!")
            time.sleep(1.5)
            os.system(limpaTela)
            print("========= .:| Inclusão de veículo |:. ========= ")
            print(f"Digite o valor do carro: {valor}")
            print(f"Digite o modelo do carro: {modelo}")
            print(f"Digite a cor do carro: {cor}")

    return valor, modelo, cor, quilometragem


def tenteInput(tipo, mensagem, mensagem_erro):
    ret = None
    while True:
        try:
            ret = tipo(input(mensagem))
        except ValueError:
            print(mensagem_erro)
            continue
        if tipo is str and ret.isdigit():
            print(mensagem_erro)
            continue

        return ret
