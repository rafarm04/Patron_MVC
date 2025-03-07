from ..Clases.User import User
from firebase.config import db

class UserDAO:
    @staticmethod
    def add_user(uid, nombre, id, rol):
        db.collection("usuarios").document(uid).set({
            "nombre": nombre,
            "id": id,
            "rol": rol
        })
        print(f"Usuario {nombre} agregado con éxito.")

    @staticmethod
    def get_user(uid):
        """Obtiene un usuario por su UID."""
        doc = db.collection("usuarios").document(uid).get()
        if doc.exists:
            return User.from_dict(uid, doc.to_dict())
        return None
    
    @staticmethod
    def get_all_users():
        """Obtiene todos los usuarios en la colección."""
        usuarios = db.collection("usuarios").stream()
        return [User.from_dict(doc.id, doc.to_dict()) for doc in usuarios]
    
    @staticmethod
    def update_user(uid, nuevos_datos):
        """Actualiza los datos de un usuario en Firestore."""
        db.collection("usuarios").document(uid).update(nuevos_datos)
        return f"Usuario {uid} actualizado."
    
    @staticmethod
    def delete_user(uid):
        """Elimina un usuario en Firestore."""
        db.collection("usuarios").document(uid).delete()
        return f"Usuario {uid} eliminado."