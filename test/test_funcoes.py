def contar_pares(numeros):
    return len([n for n in numeros if n % 2 == 0])

def inverter_dicionario(d):
    return {v: k for k, v in d.items()}

def autenticar(usuario, senha):
    usuarios_cadastrados = {
        "admin": "1234",
        "vitor": "senha123"
    }
    return usuarios_cadastrados.get(usuario) == senha
