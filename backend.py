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

# POST'S 

@app.route('/paciente', methods=['GET', 'POST'])
def paciente():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        nombre = post_data.get('nombreP')
        apellidop = post_data.get('apellidoPP')
        apellidom = post_data.get('apellidoMP')
        dni = post_data.get('dniP')
        genero = post_data.get('generoP')
        fnac = post_data.get('fnacimientoP')
        email = post_data.get('emailP')
        telef = post_data.get('telefonoP')

        print(nombre)
        print(apellidop)
        print(apellidom)
        print(dni)
        print(genero)
        print(fnac)
        print(email)
        print(telef)

        sql = "INSERT INTO Paciente (nombreP, apellidoPP, apellidoMP, dniP, generoP, fnacimientoP, emailP, telefonoP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (nombre, apellidop, apellidom, dni, genero, fnac, email, telef)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Paciente agregado!'
    return jsonify(response_object)

@app.route('/medico', methods=['GET', 'POST'])
def medico():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        nombreM = post_data.get('nombreM')
        apellidoPM = post_data.get('apellidoPM')
        apellidoMM = post_data.get('apellidoMM')
        dniM = post_data.get('dniM')
        generoM = post_data.get('generoM')
        emailM = post_data.get('emailM')
        telefonoM = post_data.get('telefonoM')
        numColegialM = post_data.get('numColegialM')

        print(nombreM)
        print(apellidoPM)
        print(apellidoMM)
        print(dniM)
        print(generoM)
        print(emailM)
        print(telefonoM)
        print(numColegialM)

        sql = "INSERT INTO Medico (nombreM, apellidoPM, apellidoMM, dniM, generoM, emailM, telefonoM, numColegialM) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (nombreM, apellidoPM, apellidoMM, dniM, generoM, emailM, telefonoM, numColegialM)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Medico agregado!'
    return jsonify(response_object)

@app.route('/cita', methods=['GET', 'POST'])
def cita():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        IdPaciente = post_data.get('IdPaciente')
        IdSchedule = post_data.get('IdSchedule')

        print(IdPaciente)
        print(IdSchedule)

        sql = "INSERT INTO Cita (IdPaciente, IdSchedule) VALUES (%s, %s)"
        data = (IdPaciente, IdSchedule)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Cita agregada!'
    return jsonify(response_object)

@app.route('/tratamiento', methods=['GET', 'POST'])  
def tratamiento():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        descripcion = post_data.get('descripcion')
        duracion = post_data.get('duracion')
        tratamiento = post_data.get('tratamiento')
        idCita = post_data.get('idCita')

        print(descripcion)
        print(duracion)
        print(tratamiento)
        print(idCita)

        sql = "INSERT INTO Tratamiento (descripcion, duracion, tratamiento, idCita) VALUES (%s, %s, %s, %s)"
        data = (descripcion, duracion, tratamiento, idCita)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Tratamiento agregado!'
    return jsonify(response_object)

@app.route('/especialidad', methods=['GET', 'POST'])
def especialidad():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        descripcion = post_data.get('descripcion')

        print(descripcion)

        sql = "INSERT INTO Especialidad (descripcion) VALUES (%s)"
        data = (descripcion)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Especialidad agregada!'
    return jsonify(response_object)

@app.route('/especialidadmedico', methods=['GET', 'POST'])
def especialidadmedico():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        idMedico = post_data.get('idMedico')
        idEspecialidad = post_data.get('idEspecialidad')
        aniosExp = post_data.get('aniosExp')

        print(idMedico)
        print(idEspecialidad)
        print(aniosExp)

        sql = "INSERT INTO EspecialidadMedico (idMedico, idEspecialidad, aniosExp) VALUES (%s, %s, %s)"
        data = (idMedico, idEspecialidad, aniosExp)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'EspecialidadMedico agregada!'
    return jsonify(response_object)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        Fecha = post_data.get('Fecha')
        Hora = post_data.get('Hora')
        IdMedico = post_data.get('IdMedico')
        IdEspecialidad = post_data.get('IdEspecialidad')

        print(Fecha)
        print(Hora)
        print(IdMedico)
        print(IdEspecialidad)

        sql = "INSERT INTO Schedule (Fecha, Hora, IdMedico, IdEspecialidad) VALUES (%s, %s, %s, %s)"
        data = (Fecha, Hora, IdMedico, IdEspecialidad)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Schedule agregado!'
    return jsonify(response_object)

@app.route('/compra', methods=['GET', 'POST'])
def compra():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        Fecha = post_data.get('Fecha')
        Cantidad = post_data.get('Cantidad')
        Precio = post_data.get('Precio')
        total = post_data.get('total')
        IdTratamiento = post_data.get('IdTratamiento')
        IdPaciente = post_data.get('IdPaciente')
        IdMedicamento = post_data.get('IdMedicamento')

        print(Fecha)
        print(Cantidad)
        print(Precio)
        print(total)
        print(IdTratamiento)
        print(IdPaciente)
        print(IdMedicamento)

        sql = "INSERT INTO Compra (Fecha, Cantidad, Precio, total, IdTratamiento, IdPaciente, IdMedicamento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (Fecha, Cantidad, Precio, total, IdTratamiento, IdPaciente, IdMedicamento)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Compra agregada!'
    return jsonify(response_object)

@app.route('/medicamento', methods=['GET', 'POST'])
def medicamento():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        Nombre = post_data.get('Nombre')

        print(Nombre)
        sql = "INSERT INTO Medicamento (Nombre) VALUES (%s)"
        data = (Nombre)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Medicamento agregado!'
    return jsonify(response_object)



if __name__ == '__main__':
    app.run(port = 5000, debug = True)