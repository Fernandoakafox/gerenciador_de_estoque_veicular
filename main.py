from listaDinamica import ListaEncadeada
import menu
import time

def main():
    limpaTela = menu.telaDeInicio()

    lista = ListaEncadeada()
    codigoIdentificacao = 1

    menu.menuPrincipal(lista, codigoIdentificacao, limpaTela)

main()
