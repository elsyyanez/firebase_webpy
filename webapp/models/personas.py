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