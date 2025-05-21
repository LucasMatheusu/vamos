# Menu da padaria com os produtos disponíveis e seus preços
menu = {
    "Pão": 1.50,
    "Bolo": 5.00,
    "Café": 2.00,
    "Torta": 3.50
}


def exibir_menu():
    """
    Exibe o menu de produtos disponíveis.
    """
    print("\n*** Menu da Padaria ***")
    for item, preco in menu.items():  # Itera sobre os itens do dicionário menu
        print(f"{item}: R$ {preco:.2f}")  # Exibe o nome e preço formatado (2 casas decimais)
    print()


def calcular_total(pedidos):
    """
    Calcula o total do pedido com base nos itens e quantidades escolhidos.

    :param pedidos: Dicionário com itens e suas quantidades.
    :return: Valor total do pedido.
    """
    total = 0
    for item, quantidade in pedidos.items():  # Itera sobre os itens do pedido
        total += menu[item] * quantidade  # Multiplica o preço do item pela quantidade
    return total


def main():
    """
    Função principal que controla o fluxo do programa.
    """
    pedidos = {}  # Dicionário para armazenar os itens e as quantidades escolhidas pelo cliente

    exibir_menu()  # Chama a função para exibir o menu

    while True:
        # Captura a escolha do cliente, padronizando para iniciar com maiúscula
        escolha = input("Digite o nome do item (ou 'sair' para finalizar): ").capitalize()

        if escolha == 'Sair':  # Verifica se o cliente quer encerrar o pedido
            break

        if escolha in menu:  # Verifica se o item está no menu
            # Solicita a quantidade desejada para o item
            quantidade = int(input(f"Quantos {escolha}(s) você quer? "))
            pedidos[escolha] = pedidos.get(escolha, 0) + quantidade  # Atualiza a quantidade no pedido
        else:
            print("Item não encontrado no menu. Tente novamente.")

    if pedidos:
        # Mostra o resumo do pedido
        print("\n*** Resumo do Pedido ***")
        for item, quantidade in pedidos.items():
            print(f"{item}: {quantidade} x R$ {menu[item]:.2f} = R$ {menu[item] * quantidade:.2f}")

        # Calcula e exibe o total
        total = calcular_total(pedidos)
        print(f"\nTotal a pagar: R$ {total:.2f}")

        # Solicita o valor pago e calcula o troco
        pago = float(input("Digite o valor pago: R$ "))
        if pago >= total:
            troco = pago - total
            print(f"Troco: R$ {troco:.2f}")
        else:
            print("Valor insuficiente. Pedido cancelado.")
    else:
        print("Nenhum pedido realizado. Obrigado por visitar!")


if __name__ == "__main__":
    main()
