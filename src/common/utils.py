from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api
from flask_jwt_extended import JWTManager

# Declaracion global del objeto de SQLAlchemy
db = SQLAlchemy()

# Declaracion global de Marshmallow
ma = Marshmallow()

# localhost/api/v1/***
api = Api(prefix='/api/v1')

# Seguridad
jwt = JWTManager()
