from firebase.config import auth

def registrar_usuario(email, password):
    user = auth.create_user(email=email, password=password)
    return user.uid

def obtener_usuario(uid):
    return auth.get_user(uid)
