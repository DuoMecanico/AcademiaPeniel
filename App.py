from flask import Flask
from flask import render_template,request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='sql3.freesqldatabase.com'
app.config['MYSQL_DATABASE_USER']='sql3429613'
app.config['MYSQL_DATABASE_PASSWORD']='culEBYFNzt'
app.config['MYSQL_DATABASE_DB']='sql3429613' 
mysql.init_app(app)

@app.route('/')
def index():

    sql ="INSERT INTO `empleados` Values ('NULL',%s, %s,%s)"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template('estudiantes/layout.html')

@app.route('/create')
def create():
    return render_template('estudiantes/create.html')
@app.route('/formulario')
def formulario():
    return render_template('estudiantes/formulario.html')

@app.route('/inscribete')
def inscribete():
    return render_template('inscribete.html')

@app.route('/store', methods=['POST'])
def storage():
    _nombre=request.form['Nombre']#saca los datos de las variables creadas en crate.html
    _apellido=request.form['Apellido']
    _nacionalidad=request.form['Nacionalidad']
    _dni=request.form['PASAPORTE']
    _edad=request.form['Edad']
    _tefelono=request.form['Telefono']
    _telefonoContacto=request.form['TelefonoDeContacto']

    #Curso
    if request.form.getlist('Idiomas') == 'Espanol':
        _Curso = request.form['Idiomas']
    else:
        _Curso = request.form['Idiomas']

    #Horario
    if request.form.getlist('Horario') == "8:00 am - 10:00 am":
        _Horario = request.form['Horario']

    elif request.form.getlist('Horario') == "10:00 am a 12:00 pm":
        _Horario = request.form['Horario']

    elif request.form.getlist('Horario') == "2:00 pm - 4:00pm":
        _Horario = request.form['Horario']

    elif request.form.getlist('Horario') == "4:00 pm - 6:00 pm":
        _Horario = request.form['Horario']

    elif request.form.getlist('Horario') == "6:00 pm - 8:00 pm":
        _Horario = request.form['Horario']

    elif request.form.getlist('Horario') == "SAB. 9 a. M. - 12 p. M":
        _Horario = request.form['Horario']

    else:
        _Horario = request.form['Horario']

    #Salud

    if len(request.form['Enfermedad']) >= 1:
        _Enfermedad = request.form['Enfermedad']
    else:
        _Enfermedad = "No"
    
    #TipoDeSangre

    if len(request.form['TipoSangre']) >= 1:
        _TipoSangre = request.form['TipoSangre']
    else:
        print()

    #¿Cómo se enteró de nosotros?
    if request.form.getlist('Medios') == "Facebook":
        _Medio = request.form['Medios']

    elif request.form.getlist('Medios') == "Instagram":
        _Medio = request.form['Medios']

    elif request.form.getlist('Medios') == "Volante":
        _Medio = request.form['Medios']

    elif request.form.getlist('Medios') == "Marca":
        _Medio = request.form['Medios']

    elif request.form.getlist('Medios') == "Conocido":
        _Medio = request.form['Medios']

    else:
        _Medio = request.form['Medios']

    #NivelAcademico
    if request.form.getlist('Medios') == "Básico":
        _NivelAcademico = request.form['NivelAcademico']

    elif request.form.getlist('Medios') == "Bachillerato":
        _NivelAcademico = request.form['NivelAcademico']

    else:
        _NivelAcademico = request.form['NivelAcademico']

    sql ="INSERT INTO `Alumnos`(`ID`, `Nombre`,`Apellido`, `Nacionalidad`, `Pasaporte`,`Edad`, `Telefono`, `TelefonoConctato`,`Curso`,`Horario`,`SufreEnfermedad`,`TipoSangre`,`ComoSeEntero`,`NivelAcademico`) Values ('NULL',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    datos=(_nombre,_apellido,_nacionalidad,_dni,_edad,_tefelono,_telefonoContacto,_Curso,_Horario,_Enfermedad,_TipoSangre,_Medio,_NivelAcademico)#Le envia los daots al slq

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)#Introducce los datos en la consulta 
    conn.commit()

    return render_template('inscribete.html')






if __name__ == '__main__':
    app.run(debug=True)