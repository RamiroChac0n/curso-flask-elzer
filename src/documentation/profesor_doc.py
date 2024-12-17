from flask_restx import fields
from src.common.utils import api

Profesor_doc =api.model('Profesor_doc',{
    'id_profesor': fields.Integer(description='ID del profesor', required=True),
    'nombre': fields.String(description='Nombre del profesor', required=True),
    'apellido': fields.String(description='Apellido del profesor', required=True),
    'registro': fields.Integer(description='Identificación del registro personal', required=True),
    'id_usuario': fields.Integer(description='El identificador del usuario', required=True) 
})

Profesor_create_doc = api.model('Profesor_create_doc', {
    'nombre': fields.String(description='Nombre del profesor', required=True),
    'apellido': fields.String(description='Apellido del profesor', required=True),
    'registro': fields.Integer(description='Identificación del registro personal', required=True),
    'id_usuario': fields.Integer(description='El identificador del usuario', required=True)      
})