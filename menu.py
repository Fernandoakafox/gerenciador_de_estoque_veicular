import os
import time
import modules
from listaDinamica import No
from modules import tenteInput


def menuPrincipal(lista, codigoIdentificacao, limpaTela):
    os.system(limpaTela)
    while True:
        print("\n\n ========= .:| Menu |:. ========= ")
        print(" 1 - Inserir no início")
        print(" 2 - Inserir no final")
        print(" 3 - Exibir a lista")
        print(" 4 - Pesquisar")
        print(" 5 - Excluir um registro")
        print(" 6 - Gerar Registros")
        print(" 0 - Sair")
        print(" ================================ ")

        while (True):
            try:
                opcao = int(input("Digite uma opção: "))
                if isinstance(opcao, int):
                    break
            except ValueError:
                os.system(limpaTela)
                print("\n\n ========= .:| Menu |:. ========= ")
                print(" 1 - Inserir no início")
                print(" 2 - Inserir no final")
                print(" 3 - Exibir a lista")
                print(" 4 - Pesquisar")
                print(" 5 - Excluir um registro")
                print(" 6 - Gerar Registros")
                print(" 0 - Sair")
                print(" ================================ ")
                print("Digite um numero valido!")

        #lembre-se, em python não vai break no match case
        match opcao:
            case 1:
                os.system(limpaTela)
                print("========= .:| Inclusão de veículo |:. ========= ")
                valor, modelo, cor, quilometragem = modules.entradaDados(
                    limpaTela)
                novoNo = No(codigoIdentificacao, valor, modelo, cor,
                            quilometragem)
                codigoIdentificacao += 1
                lista.inserirInicio(novoNo)
                os.system(limpaTela)
                print("Veículo cadastrado com sucesso!")
                time.sleep(0.5)

            case 2:
                os.system(limpaTela)
                print("========= .:| Inclusão de veículo |:. ========= ")
                valor, modelo, cor, quilometragem = modules.entradaDados(
                    limpaTela)
                novoNo = No(codigoIdentificacao, valor, modelo, cor,
                            quilometragem)
                codigoIdentificacao += 1
                lista.inserirFinal(novoNo)
                os.system(limpaTela)
                print("Veículo cadastrado com sucesso!")
                time.sleep(0.5)

            # Mostra a lista de carros
            case 3:
                os.system(limpaTela)
                if not lista.listaVazia():
                    lista.mostrarLista()
                    enter = input(
                        "Pressione enter para voltar ao menu principal: ")
                else:
                    print("Lista vazia!")
                    enter = input(
                        "Pressione enter para voltar ao menu principal: ")

            # Mostra o menu de pesquisas
            case 4:
                os.system(limpaTela)
                if not lista.listaVazia():
                    menuDePesquisa(lista, limpaTela)
                else:
                    print("Lista vazia!")
                    enter = input(
                        "Pressione enter para voltar ao menu principal: ")

            # Exclui um registro da lista
            case 5:
                os.system(limpaTela)
                lista.excluirNo()
                opcao = input(
                    "Pressione enter para voltar ao menu principal: ")

            # Gera registros para teste
            case 6:
                os.system(limpaTela)
                codigoIdentificacao += lista.gerarRegistrosTeste(codigoIdentificacao)
                print("Registros gerados com sucesso!")
                opcao = input(
                    "Pressione enter para voltar ao menu principal: ")

            case 0:
                print("Saindo do programa....")
                return

            case _:
                print("Opção inválida!")

        #parada de tela
        time.sleep(0.8)
        #limpa tela
        os.system(limpaTela)


def menuDePesquisa(lista, limpaTela):
    print("\n\n ===== .:| Filtros de pesquisa |:. ===== ")
    print(" 1 - Até tal valor")
    print(" 2 - Modelo")
    print(" 3 - Cor")
    print(" 4 - Até tal quilometragem")
    print(" 5 - Todos")
    print(" 0 - Voltar ao menu principal")
    print("=====================================")

    opcao = tenteInput(int, "Digite o numero relativo ao filtro de pesquisa: ",
                       "Digite uma opcao válida!")

    os.system(limpaTela)
    match opcao:
    # Pesquisa até tal valor
        case 1:
            v = tenteInput(float, "Digite o valor: ", "Digite um valor válido")
            lista.pesquisarAteValor(v)

        # Pesquisa por modelo
        case 2:
            m = tenteInput(str, "Digite o modelo: ", "Digite um modelo válido")
            lista.pesquisarPorModelo(m, limpaTela)

        # Pesquisa por cor
        case 3:
            c = tenteInput(str, "Digite uma cor: ", "Digite uma cor válida")
            lista.pesquisarPorCor(c, limpaTela)

        # Pesquisa até tal quilometragem
        case 4:
            q = tenteInput(int, "Digite o valor: ", "Digite um valor válido")
            lista.pesquisarAteQuilometragem(q, limpaTela)

        case 5:
            lista.pesquisarTodos(limpaTela)

        case 0:
            return


def telaDeInicio():
    while True:
        print(
            "\n\n ========= .:| Gerenciamento de estoque de veículos |:. ========= "
        )
        print("V1.12 - Release 21/03/2024")

        print("( 1 ) Execução em ambiente Windows")
        print("( 2 ) Execução em ambiente Linux / Mac")
        while True:
            try:
                opcao = int(input("Digite uma opção: "))
                if isinstance(opcao, int):
                    break
            except ValueError:
                print("Digite uma opção valida!")
        match (opcao):
            case 1:
                return 'cls'
            case 2:
                return 'clear'
            case _:
                print("Opção invalida!")
                time.sleep(0.5)
                os.system('cls')
                os.system('clear')
