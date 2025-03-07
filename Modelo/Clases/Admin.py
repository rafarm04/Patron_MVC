import Modelo.Clases.User as User

class Admin(User):
    def __init__(self, nombre, id):
        super().__init__(nombre, id, "Administrador")

    def gestionar_horarios(self):
        print("Gestionando horarios")

    def monitorear_citas(self):
        print("Monitoreando citas")