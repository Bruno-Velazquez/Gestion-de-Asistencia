from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///asistencia.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    rol = db.Column(db.String(20))  # alumno, docente, admin

class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    fecha = db.Column(db.String(20))
    presente = db.Column(db.Boolean)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/usuarios', methods=['POST'])
def registrar_usuario():
    data = request.json
    nuevo = Usuario(nombre=data['nombre'], rol=data['rol'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Usuario registrado"}), 201

@app.route('/asistencia', methods=['POST'])
def marcar_asistencia():
    data = request.json
    asistencia = Asistencia(usuario_id=data['usuario_id'], fecha=datetime.today().strftime('%Y-%m-%d'), presente=data['presente'])
    db.session.add(asistencia)
    db.session.commit()
    return jsonify({"mensaje": "Asistencia registrada"})

@app.route('/asistencias/<int:usuario_id>', methods=['GET'])
def ver_asistencia(usuario_id):
    registros = Asistencia.query.filter_by(usuario_id=usuario_id).all()
    return jsonify([{"fecha": r.fecha, "presente": r.presente} for r in registros])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
