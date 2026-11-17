from bson.objectid import ObjectId
from bson.errors import InvalidId
from mymongo import db

col = db.produto
col_vendedor = db.vendedor


def to_object_id(valor):
    try:
        return ObjectId(valor)
    except InvalidId:
        print("ID inválido")
        return None


def montar_vendedor(vendedor):
    return {
        "nome": vendedor.get("nome"),
        "cpf_cnpj": vendedor.get("cpf_cnpj"),
        "email": vendedor.get("email")
    }


def mostrar_produto(p):
    v = p.get("vendedor", {})
    print("-" * 40)
    print("Produto:", p.get("nome"))
    print("Descrição:", p.get("descricao"))
    print("Preço: R$", p.get("preco"), "| Quantidade:", p.get("quantidade"))
    print("Vendedor:", v.get("nome"), "| CPF/CNPJ:", v.get("cpf_cnpj"),
          "| E-mail:", v.get("email"))


def create_produto():
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    nome_vendedor = input("Nome do vendedor: ")
    vendedor = col_vendedor.find_one({"nome": nome_vendedor})
    if vendedor is None:
        print("Vendedor nao encontrado")
        return

    produto = {
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "quantidade": quantidade,
        "vendedor_id": vendedor["_id"],
        "vendedor": montar_vendedor(vendedor)
    }

    x = col.insert_one(produto)
    print("Inserido:", x.inserted_id)


def read_produto(nome=""):
    nome = nome or input("Nome (vazio para todos): ")
    if len(nome):
        docs = col.find({"nome": nome})
    else:
        docs = col.find().sort("nome")
    for d in docs:
        mostrar_produto(d)


def update_produto(nome):
    produto = col.find_one({"nome": nome})
    if produto is None:
        print("Nao encontrado")
        return

    mostrar_produto(produto)

    nome = input("Novo nome: ")
    if len(nome):
        produto["nome"] = nome

    descricao = input("Nova descrição: ")
    if len(descricao):
        produto["descricao"] = descricao

    preco = input("Novo preço: ")
    if len(preco):
        produto["preco"] = float(preco)

    quantidade = input("Nova quantidade: ")
    if len(quantidade):
        produto["quantidade"] = int(quantidade)

    r = col.update_one({"_id": produto["_id"]}, {"$set": produto})
    print("Alterados:", r.modified_count)


def delete_produto(nome):
    r = col.delete_one({"nome": nome})
    print("Deletados:", r.deleted_count)