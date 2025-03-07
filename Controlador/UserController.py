from ..Modelo.DAO.UserDAO import UserDAO
from ..Modelo.Clases.User import User

class UsuarioController:
    def __init__(self):
        self.usuario_dao = UserDAO()  # Conexión con la base de datos

    def registrar_usuario(self, nombre, id, rol):
        """Crea un nuevo usuario y lo guarda en la base de datos"""
        nuevo_usuario = User(nombre, id, rol)
        self.usuario_dao.agregar_usuario(nuevo_usuario)
        print(f"Usuario {nombre} registrado con éxito.")

    def obtener_usuario(self, id):
        """Busca un usuario en la base de datos por ID"""
        usuario = self.usuario_dao.obtener_usuario(id)
        if usuario:
            return usuario
        else:
            print("Usuario no encontrado.")

    def listar_usuarios(self):
        """Muestra todos los usuarios registrados"""
        usuarios = self.usuario_dao.obtener_todos()
        for usuario in usuarios:
            print(usuario)
