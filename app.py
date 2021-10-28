from flask import Flask, request, render_template,flash
from flask import render_template as render
from flask import redirect
from sqlite3 import Error
import os

from forms import Login
import gestorDB 
import utils

app = Flask(__name__)
app.secret_key = os.urandom( 24 )
sesion_iniciada = False;

@app.route("/", methods=['GET', 'POST'])
def inicio():
    #Pagina index para inciar sesión
    return render("index.html")

#login - conexión base de datos 
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            db = gestorDB.get_db()
            error = None
            username = request.form['codigo']
            password = request.form['password']
            rol = request.form['rol']
            

            if not username:
                error = 'Debes ingresar el usuario'
                flash( error )
                return render_template( 'index.html' )

            if not password:
                error = 'Contraseña requerida'
                flash( error )
                return render_template( 'index.html' )
            
            NombreRol=""
            if rol =="1":
                NombreRol="estudiante"
            elif rol =="2":
                NombreRol ="profesor"
            else:
                NombreRol="administrador"

            user = db.execute(
                'SELECT * FROM '+NombreRol+' WHERE  ID = ? AND password = ? ', (username, password)
            ).fetchone()

            print(rol,NombreRol)
            # print(user)

            if user is None:
                error = 'Usuario o contraseña inválidos'
            else:

                home =''
                
                if rol == "1":
                    home='homeEstudiante'
                elif rol == "2":
                    home ='homeProfesor'
                else:
                   home='dashboard'
                    
                return redirect(home)

            flash( error )
        return render_template( 'index.html' )
    except:
        return render_template( 'index.html' )

@app.route('/recordarPass', methods=['GET'])
def recordar_pass():
    return render("recordarPass.html")



@app.route('/dashboard/<rol_usuario>', methods=['GET', 'POST'])
def usuario(rol_usuario):
    if rol_usuario == "estudiante":
        return render("homeEstudiante.html")
    elif rol_usuario == "profesor":
        return render("homeProfesor.html")
    elif rol_usuario == "admin":
        return render("dashboard.html")



#ADMINISTRAD0R----------------------------------------------------------------------------------------------
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render("dashboard.html")

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    return render("registro.html")

@app.route("/BuscarCursosAdministrador", methods=['GET', 'POST'])
def BuscarCursosAdministrador():
    return render("BuscarCursosAdministrador.html")


@app.route("/BuscarUsuarioAdministrador", methods=['GET', 'POST'])
def BuscarUsuarioAdministrador():
    return render("BuscarUsuario.html")


@app.route("/BuscarAsignaturaAdministrador", methods=['GET', 'POST'])
def BuscarAsignaturaAdministrador():
    return render("BuscarAsignaturasAdministrador.html")


@app.route("/crearCursos", methods=['GET', 'POST'])
def crearCursos():
    return render("crearCursos.html")


@app.route("/crearAsignatura", methods=['GET', 'POST'])
def crearAsignatura():
    return render("crearAsignatura.html")


@app.route("/informacionAdministrador", methods=['GET', 'POST'])
def informacionAdministrador():
    return render("informacionAdministrador.html")

#Integración de registro de usuarios 
@app.route( '/registar', methods=('GET', 'POST') )
def registar():
    try:
        if request.method == 'POST':
            print('ENTRA')
            codigo = request.form['codigo']
            name = request.form['name']
            apellido = request.form['apellido']
            tipoDocumento=request.form['tipoDocumento']
            documento = request.form['num_doc']
            password = request.form['password']
            email = request.form['mail']
            fechaNacimiento= request.form['fecha_nac']
            carrera = request.form['carrera']
            tipoUsuario = request.form['TipoUsuario']

            error = None
            db = gestorDB.get_db()

            if not name:
                error = 'Debes ingresar el nombre del usuario'
                flash( error )
                return render_template( 'registro.html' )
            
            if not apellido:
                error = 'Debes ingresar el nombre del usuario'
                flash( error )
                return render_template( 'registro.html' )

            if not utils.isPasswordValid( password ):
                error = 'La contraseña debe contenir al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash( error )
                print(error)
                return render_template( 'registro.html' )

            if not utils.isEmailValid( email ):
                error = 'Correo invalido'
                flash( error )
                print(error)
                return render_template( 'registro.html' )

            # if db.execute( 'SELECT ID FROM estudiante WHERE email = ?', (email) ).fetchone() is not None:
            #     error = 'El correo ya existe'.format( email )
            #     flash( error )
            #     return render_template( 'auth/registro.html' )

            print(error)
            print("ENTRAAA")
            strsql = "insert into estudiante (codigo, password,tipoDeDocumento, cedula, nombres, apellidos, email, fechaDeNacimiento, carrera) values("+codigo+",'"+password+"',"+tipoDocumento+","+documento+", '"+name+"', '"+apellido+"', '"+email+"', "+fechaNacimiento+",'"+carrera+"' )"
            db.execute(strsql)
            db.commit()

            flash( 'Usuario creado' )
            return render_template( 'registro.html' )
        return render_template( 'registro.html' )
    except:
        return render_template( 'registro.html' )
#Fin de creacion de usuarios 

#Integración de la creación de asignatura
@app.route( '/registro_asignatura', methods=('GET', 'POST') )
def registro_asignatura():
    try:
        if request.method == 'POST':
            print('ENTRA')
            name = request.form['nombre_asignatura']
            codigo = request.form['CodigoAsignatura']
            creditos = request.form['NumeroCreditos']
            maxEstudiante = request.form['MaxEstudiante']
            detalle= request.form['DetalleAsignatura']

            error = None
            db = gestorDB.get_db()
            if not utils.isUsernameValid(name):
                error = "El nombre debe ser alfanumerico o incluir solo '.','_','-'"
                flash( error )
                return render_template( 'crearAsignatura.html' )

            
            if not detalle:
                error = 'Debes ingresar una descripción'
                flash( error )
                return render_template( 'crearAsignatura.html' )


            # if db.execute( 'SELECT codigo FROM asignatura WHERE codigo = ?', (codigo) ).fetchone() is not None:
            #     error = 'El codigo ya existe'.format( codigo )
            #     flash( error )

                return render_template( 'auth/crearAsignatura.html' )
            print(error)
            strsql = "insert into asignatura (codigo, nombre, creditos,detalle) values("+codigo+", '"+name+"', "+creditos+", '"+detalle+"' )"
            db.execute(strsql)
            db.commit()

            flash( 'Asignatura creada' )
            return render_template( 'crearAsignatura.html' )
        return render_template( 'crearAsignatura.html' )
    except:
        return render_template( 'crearAsignatura.html' )
#Fin de creacion de ruta del formulario de creación de asignaturas

#Creacion de cursos 
@app.route( '/registro_curso', methods=('GET', 'POST') )
def registro_curso():
    try:
        if request.method == 'POST':
            print('ENTRA')
            name = request.form['nombreCurso']
            codigo = request.form['CodigoCurso']
            profesorAsociado = request.form['ProfesorCurso']
            maxEstudiante = request.form['MaxEstudiante'] 
            asignatura = request.form['AsignaturaAsociada']

            error = None
            db = gestorDB.get_db()
            if not utils.isUsernameValid(name):
                error = "El nombre debe ser alfanumerico o incluir solo '.','_','-'"
                flash( error )
                return render_template( 'crearCursos.html' )


            # if db.execute( 'SELECT codigo FROM asignatura WHERE codigo = ?', (codigo) ).fetchone() is not None:
            #     error = 'El codigo ya existe'.format( codigo )
            #     flash( error )

             #   return render_template( 'auth/crearAsignatura.html' )
            #print(error)
            strsql = "insert into curso (codigo, nombre, asignatura,maxEstudiante,profesor) values("+codigo+", '"+name+"', '"+asignatura+"',"+maxEstudiante+", '"+profesorAsociado+"' )"
            db.execute(strsql)
            db.commit()

            flash( 'Curso creada' )
            return render_template( 'crearCursos.html' )
        return render_template( 'crearCursos.html' )
    except:
        return render_template( 'crearCursos.html' )
#Fin de creacion de ruta de creacion de curso

#PAGINAS DE PROFESOR-------------------------------------------------------------------------------------

@app.route("/homeProfesor", methods=['GET', 'POST'])
def homeProfesor():
    return render("homeProfesor.html")

@app.route("/misCursosProfesor", methods=['GET', 'POST'])
def misCursosProfesor():
    return render("misCursosProfesor.html")

@app.route("/informacionProfesor", methods=['GET', 'POST'])
def informacionProfesor():
    return render("informacionProfesor.html")

@app.route("/cursoProfesor", methods=['GET', 'POST'])
def cursoProfesor():
    return render("cursoProfesor.html")

@app.route("/detalleActividadProfesor", methods=['GET', 'POST'])
def detalleActividadProfesor():
    return render("detalleActividadProfesor.html")

#PAGINAS DE Estudiante----------------------------------------------------------------------------------

@app.route("/homeEstudiante", methods=['GET', 'POST'])
def homeEstudiante():
    return render("homeEstudiante.html")

@app.route("/registroAsignatura", methods=['GET', 'POST'])
def registroAsignatura():
    return render("registroAsignatura.html")

@app.route("/verNotasEstudiante", methods=['GET', 'POST'])
def verNotasEstudiante():
    return render("verNotasEstudiante.html")

@app.route("/informacionEstudiante", methods=['GET', 'POST'])
def informacionEstudiante():
    return render("informacionEstudiante.html")

@app.route("/cursoEstudiante", methods=['GET', 'POST'])
def cursoEstudiante():
    return render("cursoEstudiante.html")

@app.route("/detalleActividadEstudiante", methods=['GET', 'POST'])
def detalleActividadEstudiante():
    return render("detalleActividadEstudiante.html")

@app.route("/retroalimentacionEstudiante", methods=['GET', 'POST'])
def dretroalimentacionEstudiante():
    return render("retroalimentacionEstudiante.html")

#----------------------------------------------------------------------------------------------------------



@app.route('/perfil', methods=['GET'])
def perfil():
    return render("dashboard.html")



@app.route('/editar', methods=['GET', 'POST'])
def editar():
    return render("informacionEstudiante.html")

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