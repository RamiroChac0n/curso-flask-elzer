from flask_restx import fields
from src.common.utils import api

Usuario_doc =api.model('Usuario_doc',{
    'id_usuario': fields.Integer(description='ID del usuario', required=True),
    'nombre': fields.String(description='Nombre del usuario', required=True),
    'correo': fields.String(description='Correro del usuario', required=True),
    'password': fields.String(description='Contraseña de acceso', required=True),
    'ultimo_acceso': fields.DateTime(description='Último acceso del usuario', required=True),
    'id_rol': fields.Integer(description='El ID del rol del usuario', required=True)   
})

Usuario_create_doc = api.model('Usuario_create_doc', {
    'nombre': fields.String(description='Nombre del usuario', required=True),
    'correo': fields.String(description='Correo del usuario', required=True),
    'password': fields.String(description='Contraseña de acceso', required=True),
    'ultimo_acceso': fields.DateTime(description='Último acceso del usuario', required=True),
    'id_rol': fields.Integer(description='El ID del rol del usuario', required=True)     
})