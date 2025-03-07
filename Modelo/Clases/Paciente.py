import User
import Cita

class Paciente(User):
    def __init__(self, nombre, id, motivo):
        super().__init__(nombre, id, "Paciente")
        self.motivo = motivo
        self.citas = []

    def agendar_cita(self, fecha, motivo):
        nueva_cita = Cita(fecha, motivo)
        self.citas.append(nueva_cita)
        return nueva_cita

    def consultar_estado_cita(self):
        return [cita.estado for cita in self.citas]
