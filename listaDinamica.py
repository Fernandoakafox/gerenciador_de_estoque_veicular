import os
import random
import modules


class No:

    def __init__(self, identificacao, valor, modelo, cor, quilometragem):
        self.codIdentificacao = identificacao
        self.valor = valor
        self.modelo = modelo
        self.cor = cor
        self.quilometragem = quilometragem
        self.proximo = None

    def exibirInformacoes(self):
        print(f"\n\n ======= .:| codigo: {self.codIdentificacao} |:. ======= ")
        print(" Modelo: %s " % (self.modelo))
        print(" Valor: R$ %d " % (self.valor))
        print(" Cor:  %s " % (self.cor))
        print(" Quilometragem: %d " % (self.quilometragem))
        print(" ================================= ")


class ListaEncadeada:

    def __init__(self):
        self.primeiro = None
        self.quantidadeDeNos = 0

    def mostrarLista(self):
        aux = self.primeiro
        while aux != None:
            aux.exibirInformacoes()
            aux = aux.proximo

    def listaVazia(self):
        #se a cabeça da lista aponta para None, retorna True, do contrario retorna false
        return self.primeiro is None

    # Inserções de nós na lista  ==================================================

    def inserirInicio(self, novoNo):
        # novo nó aponta para quem a cabeça da lista apontava
        novoNo.proximo = self.primeiro
        # cabeça da lista aponta para novo nó
        self.primeiro = novoNo
        self.quantidadeDeNos += 1

    def inserirFinal(self, novoNo):
        aux = self.primeiro

        if aux == None:
            self.primeiro = novoNo
            self.quantidadeDeNos += 1
            return

        while aux.proximo != None:
            aux = aux.proximo
        aux.proximo = novoNo
        self.quantidadeDeNos += 1

    # Pesquisar - até tal Valor =======================================================

    def pesquisarAteValor(self, valor):

        print(f" -> Veículos com valor até R$ {valor} :")
        aux = self.primeiro

        flag = 0
        while aux != None:
            if aux.valor <= valor:
                flag = 1
                aux.exibirInformacoes()
            aux = aux.proximo
        if flag == 0:
            print(
                f"Não foram encontrados veiculos com o valor até R$ {valor}!")
        opcao = input("Pressione enter para voltar: ")

    # Pesquisar - Modelo =======================================================

    def pesquisarPorModelo(self, modelo, limpaTela):
        os.system(limpaTela)

        print(f" -> Veículos do modelo {modelo}:")

        aux = self.primeiro

        flag = 0
        while aux != None:
            if aux.modelo.lower() == modelo.lower():
                aux.exibirInformacoes()
                flag = 1
            aux = aux.proximo

        if flag == 0:
            print(f"Não foram encontrados veículos do modelo {modelo}!")
        opcao = input("Pressione enter para voltar: ")

    # Pesquisar - Até tal quilometragem ================================================

    def pesquisarAteQuilometragem(self, quilometragem, limpaTela):
        os.system(limpaTela)

        print(f" -> Veículos com até {quilometragem} km :")

        aux = self.primeiro

        flag = 0
        while aux != None:
            if aux.quilometragem <= quilometragem:
                flag = 1
                aux.exibirInformacoes()
            aux = aux.proximo

        if flag == 0:
            print(
                f"O Carro com quilometragem {quilometragem} NÃO foi encontrado!"
            )
        opcao = input("Pressione enter para voltar: ")

    # Pesquisar - Por cor ================================================
    def pesquisarPorCor(self, cor, limpaTela):
        os.system(limpaTela)

        print(f" -> Veículos com cor {cor}")

        aux = self.primeiro

        flag = 0
        while aux != None:
            if aux.cor.lower() == cor.lower():
                flag = 1
                aux.exibirInformacoes()
            aux = aux.proximo

        if flag == 0:
            print(f"O Carro com a cor {cor} NÃO foi encontrado!")
        opcao = input("Pressione enter para voltar: ")

    # Pesquisar - Todos =======================================================
    def pesquisarTodos(self, limpaTela):
        os.system(limpaTela)

        print(f" -> Todos os veículos")
        self.mostrarLista()
        enter = input("Pressione enter para voltar ao menu principal: ")

    # Exclusão de nós da lista =======================================================

    def excluirNo(self):
        if self.listaVazia():
            print("A lista está vazia!")
            return

        codigo = modules.tenteInput(int, "Digite o codigo do carro a ser exluido: ",
                                    "Erro: Você deve digitar um valor inteiro!")

        # ponteiro ptAtual aponta para o primeiro nó da lista
        ptAtual = self.primeiro

        # armazena a string referente ao modelo do veiculo
        modeloCarro = None

        # caso o primero nó for o nó que deve ser excluido
        if ptAtual.codIdentificacao == codigo:
            # armazena modelo do carro
            modeloCarro = ptAtual.modelo
            self.primeiro = ptAtual.proximo
            self.quantidadeDeNos -= 1
            print(f"O carro modelo {modeloCarro} código {codigo} foi excluido!")
            return

        # ponteiro anterior, aponta para o primeiro nó
        ptAnterior = self.primeiro
        # ponteiro atual aponta para o segundo nó da lista
        ptAtual = self.primeiro.proximo

        # enquanto o ponteiro ptAtual estiver apontando para um nó valido
        while ptAtual != None:
            if ptAtual.codIdentificacao == codigo:
                # armazena modelo do carro
                modeloCarro = ptAtual.modelo
                ptAnterior.proximo = ptAtual.proximo
                # nó a ser exluido aponta para none, para que o python lide com ele
                ptAtual.proximo = None

                self.quantidadeDeNos -= 1
                print(f"O carro modelo {modeloCarro} codigo {codigo} foi excluido!")
                return
            # atualização de ponteiros
            ptAnterior = ptAnterior.proximo
            ptAtual = ptAtual.proximo
        print("O carro codigo %d não foi encontrado!" % (codigo))

    #=================================================================================

    # Geração de Registros para teste =======================================================
    def gerarRegistrosTeste(self, codigoIdentificacao):
        quantidade = int(
            input("Digite a quantidade de registros a serem gerados: "))

        for _ in range(quantidade):
            valor = self.gerarNumeroAleatorio(100000, 10000)
            modelo = self.gerarModeloAleatorio()
            cor = self.gerarCorAleatoria()
            quilometragem = self.gerarNumeroAleatorio(150000, 0)

            novoNo = No(codigoIdentificacao, valor, modelo, cor, quilometragem)
            self.inserirFinal(novoNo)
            codigoIdentificacao += 1

        return quantidade

    def gerarModeloAleatorio(self):
        modelo = [
            "Fusca", "Gol", "Celta", "Palio", "Corsa", "Fox", "Uno", "Fiesta",
            "Camaro", "Kwid", "Ford Ka 2013"
        ]
        return modelo[random.randint(0, len(modelo) - 1)]

    def gerarCorAleatoria(self):
        cores = [
            "Azul", "Vermelho", "Amarelo", "Verde", "Preto", "Branco", "Prata"
        ]
        return cores[random.randint(0, len(cores) - 1)]

    def gerarNumeroAleatorio(self, maximo, minimo):
        return random.randint(minimo, maximo)
