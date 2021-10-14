from flask import Flask
from flask import render_template as render
from flask import redirect

app = Flask(__name__)

sesion_iniciada = False;

@app.route("/", methods=['GET', 'POST'])
def inicio():
    #Pagina index para inciar sesión
    return render("index.html")

@app.route('/recordarPass', methods=['GET'])
def recordar_pass():
    return render("recordarPass.html")

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    return render("registro.html")

@app.route('/dashboard/<rol_usuario>', methods=['GET', 'POST'])
def usuario(rol_usuario):
    if rol_usuario == "estudiante":
        return render("homeEstudiante.html")
    elif rol_usuario == "profesor":
        return render("homeProfesor.html")
    elif rol_usuario == "admin":
        return render("dashboard.html")

@app.route('/editest', methods=['GET', 'POST'])
def editarEst():
    return render("informacionEstudiante.html")

@app.route('/buscarasign')
def buscarAsig():
    return render("BuscarAsignaturasAdministrador.html")

@app.route('/buscarcursos')
def buscarCursos():
    return render("BuscarCursosAdministrador.html")

@app.route('/editprof', methods=['GET', 'POST'])
def editarProf():
    return render("informacionProfesor.html")

@app.route('/editadmin', methods=['GET', 'POST'])
def editarProf():
    return render("informacionAdministrador.html")

@app.route('/MisCursos', methods=['GET'])
def cursos(rol_usuario):
    if rol_usuario == "estudiante":
        return render("cursoEstudiante.html")
    elif rol_usuario == "profesor":
        return render("cursoProfesor.html")
    
@app.route('/actividadest', methods=['GET', 'POST'])
def Actividades():
    return render("detalleActividadEstudiante.html")

@app.route('/actividadprof', methods=['GET', 'POST'])
def Actividades():
    return render("detalleActividadProfesor.html")

@app.route('/Notas', methods=['GET', 'POST'])
def notas():
    return render ("verNotasEstudiante.html")

@app.route('/retroprof')
def retroProf():
    return render ("retroAlimentacionProfesor.html")

@app.route('/retroest')
def retroEst():
    return render ("retroAlimentacionEstudiante.html")

@app.route('/buscaruser')
def buscarUser():
    return render("BuscarUsuario.html")

@app.route('/buscaruseradmin')
def buscarUserAdmin():
    return render("BuscarUsuarioAdministrador.html")

@app.route('/crearcursos')
def crearCursos():
    return render("crearCursos.html")

@app.route('/salir', methods=['GET'])
def salir():
    sesion_iniciada = False;
    return redirect('/inicio')

if __name__ == "__main__":
    app.run(debug=True);