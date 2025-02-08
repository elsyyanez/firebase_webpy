import web  # Carga la librería web.py
from controllers.index import Index
from controllers.personas.lista_personas import ListaPersonas # Asegúrate de que este archivo existe

urls = (
    '/', 'Index',
    '/lista_personas', 'ListaPersonas',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
