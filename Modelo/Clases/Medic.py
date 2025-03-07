import Modelo.Clases.User as User
import Modelo.Clases.Cita as Cita

class Medico(User):
    # Constructor de Medico heredando de User
    def __init__(self, nombre, id, fechas_disponibles):
        super().__init__(nombre, id, "Medico")
        self.fechas_disponibles = fechas_disponibles
        self.citas = []

    def RevisarCita(self, cita):
        print(f"Revisando cita: {cita}")

    def gestionar_cita(self, cita):
        print(f"Gestionando cita: {cita}")
