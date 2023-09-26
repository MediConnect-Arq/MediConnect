from flask import Flask, jsonify, request
from flask_cors import CORS
from flaskext.mysql import MySQL #pip install flask-mysql
import pymysql

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '2608Gaby@'
app.config['MYSQL_DATABASE_DB'] = 'hospital'
app.config['MYSQL_DATABASE_HOST'] = 'localhost' #no olvidar cambiar la ip
mysql.init_app(app)

#enable CORS
CORS(app, resources={r'/*': {'origins': ''}})

# sanity check route
@app.route('/')
def home():
    tabla = request.args.get('tabla', 'Paciente')
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM {}".format(tabla))
        data = cursor.fetchall()
        return jsonify({
            'status': 'success',
            'data': data,
            'tabla': tabla
        })
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# GET'S ALL

@app.route('/pacientes', methods=['GET'])
def pacientes():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Paciente order by idPaciente")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'Pacientes': data
    })

@app.route('/medicos', methods=['GET'])
def medicos():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Medico order by idMedico")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'Medicos': data
    })

@app.route('/citas', methods=['GET'])
def citas():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Cita order by idCita")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'Citas': data
    })

@app.route('/tratamientos', methods=['GET'])
def tratamientos():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Tratamiento order by idTratamiento")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'Tratamientos': data
    })

@app.route('/especialidades', methods=['GET'])
def especialidades():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Especialidad order by idEspecialidad")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'Especialidad': data
    })

@app.route('/especialidadmedicos', methods=['GET'])
def especialidadmedicos():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM EspecialidadMedico")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'EspecialidadMedico': data
    })

@app.route('/schedules', methods=['GET']) 
def schedules():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Schedule")
    data = cursor.fetchall()
    for row in data: 
        row['Hora'] = str(row['Hora'])
    return jsonify({
        'status': 'success',
        'Schedule': data
    })

@app.route('/compras', methods=['GET'])
def compras():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Compra")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'Compra': data
    })

@app.route('/medicamentos', methods=['GET'])
def medicamentos():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Medicamento")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'Medicamento': data
    })

#GET'S BY ID

@app.route('/paciente/<string:id>', methods=['GET', 'POST'])
def paciente_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Paciente WHERE idPaciente = %s", [id])
    row = cursor.fetchone()

    return jsonify({
        'status': 'success',
        'paciente' + id : row
    })

@app.route('/especialidad/<string:id>', methods=['GET', 'POST'])
def especialidad_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Especialidad WHERE IdEspecialidad = %s", [id])
    row = cursor.fetchone()

    return jsonify({
        'status': 'success',
        'especialidad' + id: row
    })

@app.route('/medico/<string:id>', methods=['GET', 'POST'])
def medico_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Medico WHERE idMedico = %s", [id])
    row = cursor.fetchone()

    return jsonify({
        'status': 'success',
        'medico' + id: row
    })        

@app.route('/cita/<string:id>', methods=['GET', 'POST'])    
def cita_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Cita WHERE idCita = %s", [id])
    row = cursor.fetchone()
    return jsonify({
        'status': 'success',
        'cita' + id: row
    })

@app.route('/tratamiento/<string:id>', methods=['GET', 'POST'])
def tratamiento_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Tratamiento WHERE idTratamiento = %s", [id])
    row = cursor.fetchone()

    return jsonify({
        'status': 'success',
        'tratamiento' + id: row
    })

@app.route('/compra/<string:id>', methods=['GET', 'POST'])
def compra_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Compra WHERE idCompra = %s", [id])
    row = cursor.fetchone()

    return jsonify({
        'status': 'success',
        'compra' + id: row
    })

@app.route('/schedule/<string:id>', methods=['GET', 'POST'])
def schedule_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Schedule WHERE idSchedule = %s", [id])
    row = cursor.fetchone() 
    row['Hora'] = str(row['Hora'])
    return jsonify({
        'status': 'success',
        'schedule' + id: row
    })

@app.route('/medicamento/<string:id>', methods=['GET', 'POST'])
def medicamento_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Medicamento WHERE idMedicamento = %s", [id])
    row = cursor.fetchone()

    return jsonify({
        'status': 'success',
        'medicamento' + id: row
    })



if __name__ == '__main__':
    app.run(port = 5000, debug = True)