from types import MethodType
from flask import Flask

app = Flask(__name__)

lista_users = ["Juan", "Pablo", "Juliana", "Felipe"]

@app.route("/", methods=['GET', 'POST'])
def inicio():
    #Pagina index para inciar sesión
    return "Pagina index"

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    return "pagina de registro de user"

@app.route('/recordar_pass', methods=['GET'])
def recordar_pass():
    return "Pagina recordar contraseña de usuario"

@app.route('/perfil', methods=['GET'])
def perfil():
    return "pagina de perfil de ususario"

@app.route('/dashboard/<id_usuario>', methods=['GET', 'POST'])
def usuario(id_usuario):
    if id_usuario in lista_users:
        return f"DashBoard Perfil de usuario: {id_usuario}"
    else:
        return f"Error el usuario {id_usuario} no existe"

@app.route('/editar', methods=['GET', 'POST'])
def editar():
    return "Pagina editar info -ADMIN-"

@app.route('/MisCursos', methods=['GET'])
def cursos(id_usuario):
    return f"Pagina mis cursos del usuario: {id_usuario}"

@app.route('/verActividades', methods=['GET', 'POST'])
def Actividades():
    return "Pagina para crear/ver actividades de los cursos de acuerdo al rol"

@app.route('/Notas', methods=['GET', 'POST'])
def notas():
    return "Página para ver/asignar notas de acuerdo al rol"

@app.route('/calificaciones', methods=['GET', 'POST'])
def calificaciones():
    return "Pagina para registrar/ver califiacaiones finales de las asignaturas"

@app.route('/detalle', methods=['GET'])
def detalle():
    return "Pagina para ver detalle de actividades y retroalimentacion de notas"

if __name__ == "__main__":
    app.run(debug=True);