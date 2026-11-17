import usuario
import vendedor
import produto
import compra
import favorito


def menu_usuario():
    sub = 0
    while sub != 'V':
        print("1-Inserir usuário")
        print("2-Procurar usuário")
        print("3-Atualizar usuário")
        print("4-Apagar usuário")
        sub = input("Operacao (V para voltar): ")

        if sub == '1':
            usuario.create_usuario()

        elif sub == '2':
            usuario.read_usuario()

        elif sub == '3':
            nome = input("Nome: ")
            usuario.update_usuario(nome)

        elif sub == '4':
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            usuario.delete_usuario(nome, sobrenome)


def menu_vendedor():
    sub = 0
    while sub != 'V':
        print("1-Inserir vendedor")
        print("2-Procurar vendedor")
        print("3-Atualizar vendedor")
        print("4-Apagar vendedor")
        sub = input("Operacao (V para voltar): ")

        if sub == '1':
            vendedor.create_vendedor()

        elif sub == '2':
            vendedor.read_vendedor()

        elif sub == '3':
            nome = input("Nome: ")
            vendedor.update_vendedor(nome)

        elif sub == '4':
            nome = input("Nome: ")
            vendedor.delete_vendedor(nome)


def menu_produto():
    sub = 0
    while sub != 'V':
        print("1-Inserir produto")
        print("2-Procurar produto")
        print("3-Atualizar produto")
        print("4-Apagar produto")
        sub = input("Operacao (V para voltar): ")

        if sub == '1':
            produto.create_produto()

        elif sub == '2':
            produto.read_produto()

        elif sub == '3':
            nome = input("Nome: ")
            produto.update_produto(nome)

        elif sub == '4':
            nome = input("Nome: ")
            produto.delete_produto(nome)


def menu_compra():
    sub = 0
    while sub != 'V':
        print("1-Inserir compra")
        print("2-Procurar compra")
        print("3-Atualizar compra")
        print("4-Apagar compra")
        sub = input("Operacao (V para voltar): ")

        if sub == '1':
            compra.create_compra()

        elif sub == '2':
            compra.read_compra()

        elif sub == '3':
            id = input("ID: ")
            compra.update_compra(id)

        elif sub == '4':
            id = input("ID: ")
            compra.delete_compra(id)


def menu_favorito():
    sub = 0
    while sub != 'V':
        print("1-Inserir favorito")
        print("2-Procurar favorito")
        print("3-Atualizar favorito")
        print("4-Apagar favorito")
        sub = input("Operacao (V para voltar): ")

        if sub == '1':
            favorito.create_favorito()

        elif sub == '2':
            favorito.read_favorito()

        elif sub == '3':
            nome = input("Nome do usuário: ")
            favorito.update_favorito(nome)

        elif sub == '4':
            nome = input("Nome do usuário: ")
            favorito.delete_favorito(nome)


key = 0
while key != 'S':
    print("\n1-Usuario")
    print("2-Vendedor")
    print("3-Produto")
    print("4-Compra")
    print("5-Favorito")
    print("S-Sair")
    key = input("Acessar coleção: ")

    if key == '1':
        menu_usuario()

    elif key == '2':
        menu_vendedor()

    elif key == '3':
        menu_produto()

    elif key == '4':
        menu_compra()

    elif key == '5':
        menu_favorito()

print("Tchau Prof...")