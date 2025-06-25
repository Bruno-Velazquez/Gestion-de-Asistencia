# backend/models.py (parte del Integrante 2)

from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  # alumno, docente, admin

class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    fecha = db.Column(db.String(20))
    presente = db.Column(db.Boolean)
