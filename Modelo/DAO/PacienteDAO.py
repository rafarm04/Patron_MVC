from firebase.config import db
from ..Clases.Paciente import Paciente

class PacienteDAO:
    @staticmethod
    def agregar_paciente(paciente: Paciente):
        data = {
            "nombre": paciente.nombre,
            "id": paciente.id,
            "rol": paciente.rol,
            "motivo": paciente.motivo
        }
        db.collection("pacientes").document(str(paciente.id)).set(data)

    @staticmethod
    def obtener_paciente(id):
        doc = db.collection("pacientes").document(str(id)).get()
        if doc.exists:
            data = doc.to_dict()
            return Paciente(data["nombre"], data["id"], data["motivo"])
        return None
