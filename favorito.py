from mymongo import db

col_usuario = db.usuario
col_produto = db.produto


def buscar_usuario_por_nome(nome):
    usuario = col_usuario.find_one({"nome": nome})
    if usuario is None:
        print("Usuario nao encontrado")
        return None
    return usuario


def buscar_produto_por_nome(nome):
    produto = col_produto.find_one({"nome": nome})
    if produto is None:
        print("Produto nao encontrado")
        return None
    return produto


def montar_favorito(produto):
    return {
        "produto_id": produto["_id"],
        "nome": produto["nome"],
        "descricao": produto.get("descricao"),
        "preco": produto.get("preco")
    }


def create_favorito():
    usuario = buscar_usuario_por_nome(input("Nome do usuário: "))
    if usuario is None:
        return

    produto = buscar_produto_por_nome(input("Nome do produto: "))
    if produto is None:
        return

    if any(f["produto_id"] == produto["_id"] for f in usuario.get("favoritos", [])):
        print("Produto ja esta nos favoritos")
        return

    r = col_usuario.update_one(
        {"_id": usuario["_id"]},
        {"$push": {"favoritos": montar_favorito(produto)}}
    )
    print("Alterados:", r.modified_count)


def read_favorito(nome_usuario=""):
    nome_usuario = nome_usuario or input("Nome do usuário (vazio para todos): ")
    if len(nome_usuario):
        usuario = buscar_usuario_por_nome(nome_usuario)
        if usuario is None:
            return
        usuarios = [usuario]
    else:
        usuarios = col_usuario.find().sort("nome")
    for u in usuarios:
        print(u["nome"], u.get("sobrenome", ""), "->", u.get("favoritos", []))


def update_favorito(nome_usuario):
    usuario = buscar_usuario_por_nome(nome_usuario)
    if usuario is None:
        return

    antigo = buscar_produto_por_nome(input("Nome do produto favorito a trocar: "))
    if antigo is None:
        return

    novo = buscar_produto_por_nome(input("Nome do novo produto: "))
    if novo is None:
        return

    r = col_usuario.update_one(
        {"_id": usuario["_id"], "favoritos.produto_id": antigo["_id"]},
        {"$set": {"favoritos.$": montar_favorito(novo)}}
    )
    print("Alterados:", r.modified_count)


def delete_favorito(nome_usuario):
    usuario = buscar_usuario_por_nome(nome_usuario)
    if usuario is None:
        return

    produto = buscar_produto_por_nome(input("Nome do produto: "))
    if produto is None:
        return

    r = col_usuario.update_one(
        {"_id": usuario["_id"]},
        {"$pull": {"favoritos": {"produto_id": produto["_id"]}}}
    )
    print("Removidos:", r.modified_count)
