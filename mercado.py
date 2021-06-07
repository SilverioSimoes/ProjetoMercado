from typing import List, Dict
from time import sleep
from models.produto import Produto
from utils.helper import formata_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def linha(tipo, num):
    print(f'\033[36m{tipo * num}')


def texto_linha(tipo, num1, msg, num2):
    print(f'{tipo * num1} {msg} {tipo * num2}')


def texto_centralizado(num, msg):
    print(f"{msg:^{num}}")


def main() -> None:
    menu()


def menu() -> None:
    linha('=', 40)
    texto_linha('=', 13, 'Bem-Vindo(a)', 13)
    texto_linha('=', 14, 'Geek Shop', 15)
    linha('=', 40)
    print()
    print(
        'Selecione uma opção abaixo:\n'
        '\n'
        '1 - Cadastrar Produto\n'
        '2 - Listar produto\n'
        '3 - Comprar produto\n'
        '4 - Visualizar carrinho\n'
        '5 - Fechar pedido\n'
        '6 - Sair do sistema\n'
    )

    opcao: str = str(input('Informe a opção: '))
    if opcao not in '123456':
        while opcao not in '123456':
            print('Opção inválida! Tente novamente...')
            opcao: str = str(input('Informe a opção: '))

    if opcao == '1':
        cadastrar_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        comprar_produto()
    elif opcao == '4':
        visualizar_carrinho()
    elif opcao == '5':
        fechar_pedido()
    elif opcao == '6':
        print('Volte Sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(2)
        menu()


def cadastrar_produto() -> None:
    linha('=', 40)
    texto_centralizado(40, 'Cadastro de Produto')
    linha('=', 40)

    nome: str = ''
    preco: float = 0
    while not nome:
        nome: str = str(input('Informe o nome do produto: '))
    while not preco:
        preco: float = float(input('Informe o preço do produto: '))               
        produto: Produto = Produto(nome, preco)
        produtos.append(produto)
        print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        linha('-', 40)
        texto_centralizado(40, 'Lista de produtos')
        linha('-', 40)
    for produto in produtos:
        print(produto)
        linha('-', 40)
        sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho:')
        linha('-', 40)
        texto_linha('=', 13, 'Produtos disponíveis', 13)
        for produto in produtos:
            print(produto)
            linha('-', 40)
            sleep(1)
        codigo: int = int(input('Código: '))
        produto: Produto = produto_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                item_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        item_no_carrinho = True
                        sleep(2)
                        menu()
                if not item_no_carrinho:
                    prod: dict = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
    else:
        print('Ainda não existem produtos para vender.')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        texto_linha('=', 9, 'Produtos no carrinho', 9)
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                linha('-', 40)
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        texto_centralizado(40, 'Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                linha('-', 40)
                sleep(1)
            print(f'Sua fatura é {formata_moeda(valor_total)}')
            print('Volte sempre!')
            carrinho.clear()
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


def produto_codigo(codigo: int) -> Produto:
    p: Produto = int
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
#'alteração'
