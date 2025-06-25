# backend/app.py (parte del Integrante 1)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///asistencia.db'
db = SQLAlchemy(app)

from models import Usuario, Asistencia

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
    asistencia = Asistencia(
        usuario_id=data['usuario_id'],
        fecha=datetime.today().strftime('%Y-%m-%d'),
        presente=data['presente']
    )
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
