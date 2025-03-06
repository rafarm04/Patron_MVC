import firebase_admin
from firebase_admin import credentials, firestore, auth

# Cargar credenciales
cred = credentials.Certificate("firebase/firebaseConfig.json")
firebase_admin.initialize_app(cred)

# Conectar a Firestore
db = firestore.client()
