from flask_restx import fields
from src.common.utils import api

# Modelo de documentacion de swagger
login_doc = api.model('login_doc', {
    'correo': fields.String(description='El correo del usuario', required=True),
    'password': fields.String(description='Contraseña de acceso', required=True)
})

# Respuesta del login
login_token_doc = api.model('login_token_doc', {
    'token': fields.String(description='Token de acceso para el sistema', required=True)
})