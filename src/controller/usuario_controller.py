from flask_restx import Resource
from src.schemas.usuario_schema import Usuario_regla_schema, Usuario_schema
from src.documentation.usuario_doc import Usuario_create_doc, Usuario_doc
from src.documentation.error_doc import Respuesta_model_error
from flask import request
from marshmallow import ValidationError
from src.common.utils import db, api
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required
import bcrypt

class Usuario_controller(Resource):

    @api.doc(description='Permite crear usuarios del sistema')
    @api.response(201, 'Éxito, usuario creado', Usuario_doc)
    @api.response(401, 'Acceso no autorizado')
    @api.response(422, 'Entidad improcesable', Respuesta_model_error)
    @api.response(503, 'Ocurrio un problema en el sistema', Respuesta_model_error)
    @api.expect(Usuario_create_doc)
    @jwt_required()
    def post(self):
        try:
            # db.session.execute(db.select('rol')).scalar()
            # Validamos la información
            usuario_schema = Usuario_regla_schema(exclude=['id_usuario']).load(request.json)

            # Validamos con el modelo
            usuario_schema = Usuario_schema(exclude=['id_usuario'])
            usuario = usuario_schema.load(request.json)

            # Extraer la contraseña
            password = usuario.password
            # Codificacion de la cadena
            password_bytes = password.encode('utf-8')
            # Hash
            pass_cript = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            # Convertir en bytes
            usuario.password = pass_cript.decode('utf-8')

            # Agregar el usuario a la db
            db.session.add(usuario)
            db.session.commit()

            return Usuario_schema().dump(usuario), 201
        
        except IntegrityError:
            return {'message': 'El id del rol no existe en el sistema'}, 406
        except ValidationError as err:
            mensaje = ' '.join([f'{clave}: {" ".join(mensaje)}' for clave, mensaje in err.messages_dict.items()])
            return {'message': mensaje}, 422
        except Exception as err:    
            return {'message': 'Algo salio mal'+str(err)}, 503 