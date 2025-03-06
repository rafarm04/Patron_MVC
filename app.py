from flask import Flask
from firebase.database import agregar_usuario

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, Flask!"

@app.route('/agregar_usuario')
def agregar_usuario_route():
    uid = "user1"
    nombre = "Juan Pérez"
    id = 25
    rol = "medico"
    
    agregar_usuario(uid, nombre, id, rol)
    return f"Usuario {nombre} agregado con éxito."

if __name__ == '__main__':
    app.run(debug=True)
