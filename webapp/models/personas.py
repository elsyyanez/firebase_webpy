import pyrebase

config = {
  "apiKey": "AIzaSyCNzz_InZ3JOIKr0I9b3lfXDiaJTEAoHYE",
  "authDomain": "bdnube-38ec9.firebaseapp.com",
  "databaseURL": "https://bdnube-38ec9-default-rtdb.firebaseio.com",
  "storageBucket": "bdnube-38ec9.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class Personas:

    def __init__(self):
        pass

    def lista_personas(self):
        try:
            personas = db.child("personas").get()
            response = {
                "status": 200,
                "message": "Todo bien :3",
                "personas": dict(personas.val())  # Se corrigió el error de sintaxis
            }
            return response
        except Exception as error:
            response = {
                "status": 400,
                "message": "Error en el servidor",
                "personas": {}
            }
            return response  
#persona = Personas()
#print(f"{persona.lista_personas()}")
