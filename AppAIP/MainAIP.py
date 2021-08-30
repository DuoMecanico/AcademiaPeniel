from logging import debug
from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql3.freesqldatabase.com'
app.config['MYSQL_USER'] = 'sql3429613'
app.config['MYSQK_PASSWORD'] = 'culEBYFNzt'
app.config['MYSQK_DB'] = 'sql3429613'
mysql = MySQL(app)

@app.route('/')
def home ():
    return render_template('Inscribete.html')

if __name__ == '__main__':
    app.run(debug = True)



    
# def ConexionBD():
#     return pymysql.connect(host = 'sql3.freesqldatabase.com',
#                            user = 'sql3429613',
#                            passwd = 'culEBYFNzt',
#                            db =  'sql3429613'
#                            )

@app.route("/Registrar", methods=["POST"])
def Registrar():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Apellido = request.form['Apellido']
        Nacionalidad = request.form['Nacionalidad']
        Pasaporte = request.form['Pasaporte']
        Edad = request.form['Edad']
        Telefono = request.form['Telefono']
        TelefonoDeContacto = request.form['TelefonoDeContacto']
    
        cur = mysql.Connection.curso()
        cur.execute("INSERT INTO Alumnos (Nombre, Apellido, Nacionalidad, Pasaporte, Edad, Telefono, TelefonoDeContacto) VALUES (%S,%S,%S,%S,%S,%S,%S)",
                    (Nombre, Apellido, Nacionalidad, Pasaporte, Edad, Telefono, TelefonoDeContacto))
        
        mysql.commit()
        mysql.close()
    return "Recibido"
    
