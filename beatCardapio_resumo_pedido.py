def mostrar_menu_principal():
    """Mostra o menu principal."""
    print("________________________________")
    print("Menu principal:")
    print("________________________________")
    print("1 - Entradas")
    print("2 - Pratos")
    print("3 - Bebidas")
    print("4 - Sobremesas")
    print("5 - Resumo do Pedido")
    print("6 - Finalizar Pedido")
    print("7 - Sair")


def mostrar_opcoes_de_entradas():
    """Mostra as opções de entradas."""
    print("Entradas:")
    print("________________________________")
    print("1 - Salada - R$ 5.00")
    print("2 - Sopa - R$ 7.00")
    print("3 - Bruschetta - R$ 6.00")
    print("4 - Voltar ao menu principal")


def mostrar_opcoes_de_pratos():
    """Mostra as opções de pratos."""
    print("Pratos:")
    print("________________________________")
    print("1 - Lasanha - R$ 15.00")
    print("2 - Pizza - R$ 12.00")
    print("3 - Risoto - R$ 10.00")
    print("4 - Voltar ao menu principal")


def mostrar_opcoes_de_bebidas():
    """Mostra as opções de bebidas."""
    print("Bebidas:")
    print("________________________________")
    print("1 - Refrigerante - R$ 3.00")
    print("2 - Suco - R$ 4.00")
    print("3 - Água - R$ 2.00")
    print("4 - Voltar ao menu principal")


def mostrar_opcoes_de_sobremesas():
    """Mostra as opções de sobremesas."""

    print("Sobremesas:")
    print("________________________________")
    print("1 - Sorvete - R$ 6.00")
    print("2 - Torta - R$ 8.00")
    print("3 - Pudim - R$ 5.00")
    print("4 - Voltar ao menu principal")


def mostrar_resumo_do_pedido(pedido):
    """Mostra o resumo do pedido."""
    print("________________________________")
    print("Resumo do Pedido:")
    for item, valor in pedido.items():
        print("- {}: R$ {:.2f}".format(item, valor))
    print("Valor Total do Pedido: R$ {:.2f}".format(sum(pedido.values())))
    print("")


def main():
    pedido = {}

    while True:
        mostrar_menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                mostrar_opcoes_de_entradas()
                escolha = input("Escolha uma entrada ou 4 para voltar: ")
                if escolha == "4":
                    break
                elif escolha in ("1", "2", "3"):
                    pedido["Salada"] = 5.0 if escolha == "1" else 7.0 if escolha == "2" else 6.0
                else:
                    print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")

        elif opcao == "2":
            while True:
                mostrar_opcoes_de_pratos()
                escolha = input("Escolha um prato ou 4 para voltar: ")
                if escolha == "4":
                    break
                elif escolha in ("1", "2", "3"):
                    pedido["Lasanha"] = 15.0 if escolha == "1" else 12.0 if escolha == "2" else 10.0
                else:
                    print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")

        elif opcao == "3":
            while True:
                mostrar_opcoes_de_bebidas()
                escolha = input("Escolha uma bebida ou 4 para voltar: ")
                if escolha == "4":
                    break
                elif escolha in ("1", "2", "3"):
                    pedido["Suco"] = 4.0 if escolha == "2" else 3.0 if escolha == "1" else 2.0
                else:
                    print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")

        elif opcao == "4":
            while True:
                mostrar_opcoes_de_sobremesas()
                escolha = input("Escolha uma sobremesa ou 4 para voltar: ")
                if escolha == "4":
                    break
                elif escolha in ("1", "2", "3"):
                    pedido["Sorvete"] = 6.0 if escolha == "1" else 8.0 if escolha == "2" else 5.0
                else:
                    print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")

        elif opcao == "5":
            mostrar_resumo_do_pedido(pedido)
            input("Pressione Enter para continuar...")

        elif opcao == "6":
            valor_total = sum(pedido.values())
            print("Pedido Finalizado:")
            mostrar_resumo_do_pedido(pedido)
            print("Valor Total do Pedido: R$ {:.2f}".format(valor_total))
            print("Pedido finalizado. Obrigado!")
            break

        elif opcao == "7":
            print("Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
    