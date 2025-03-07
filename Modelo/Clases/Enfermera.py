import User
import Cita

class Enfermera(User):
    def __init__(self, nombre, id):
        super().__init__(nombre, id, "Enfermera")
        self.pacientes = []
    
    def actualizar_estado_cita(self, cita):
        cita.estado = "Actualizado"
        print(f"Estado de cita actualizado a: {cita.estado}")

    def registrar_signos_vitales(self, paciente, cita):
        print(f"Registrando signos vitales para {paciente.nombre} en cita {cita}")