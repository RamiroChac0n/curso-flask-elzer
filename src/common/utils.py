from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api
from flask_jwt_extended import JWTManager

# Declaracion global del objeto de SQLAlchemy
db = SQLAlchemy()

# Declaracion global de Marshmallow
ma = Marshmallow()

# 
authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Ingresa el token ingresando primero Bearer: "Bearer <token>"'
    }
}

# localhost/api/v1/***
api = Api(authorizations=authorizations, prefix='/api/v1', security='Bearer')

# Seguridad
jwt = JWTManager()
