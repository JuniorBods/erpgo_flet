import flet as ft

def cadastro():
    nome = ft.TextField(label=("Nome"))
    cpf = ft.TextField(label=("CPF"))
    rg = ft.TextField(label=("RG"))
    email = ft.TextField(label=("Email"))
    telefone = ft.TextField(label=("Telefone"))
    cep = ft.TextField(label=("CEP"))
    logradouro = ft.TextField(label=("Logradouro"))
    bairro = ft.TextField(label=("Bairro"))
    uf = ft.TextField(label=("UF"))
    cidade = ft.TextField(label=("Cidade"))
    complemento = ft.TextField(label=("Complemento"))
    numero = ft.TextField(label=("Número"))

    return ft.Column(
        controls=[
            nome,
            cpf,
            rg,
            email,
            telefone,
            cep,
            logradouro,
            bairro,
            uf,
            cidade,
            complemento,
            numero
        ]
    )