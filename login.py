# backend/auth.py (parte del Integrante 4 - opcional si se extiende)
usuarios_validos = {
    "admin": "admin123",
    "docente1": "clave123"
}

def autenticar(usuario, clave):
    return usuarios_validos.get(usuario) == clave
