class Cita:
    def __init__(self, fecha, hora, motivo, estado):
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado
    
    def mostrar_cita(self):
        print("Cita programada para: {self.fecha} a la hora {self.hora}\n {self.motivo} y actualmente está {self.estado}")