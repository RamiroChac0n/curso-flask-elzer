from flask_restx import Resource
from src.schemas.login_schema import Login_schema
from flask import request
from flask_jwt_extended import create_access_token
from src.common.utils import api
from src.documentation.error_doc import Respuesta_model_error
from src.documentation.login_doc import login_doc, login_token_doc
from marshmallow import ValidationError
from src.common.utils import db
from src.models.usuario_model import Usuario_model_db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound  
from src.schemas.usuario_schema import Usuario_schema
import datetime
import bcrypt

class Login_controller(Resource):

    @api.doc(description='Permite loguearse en el sistema')
    @api.response(200, 'Éxito, token de acceso', login_token_doc)
    @api.response(503, 'Ocurrió un problema en el sistema', Respuesta_model_error)
    @api.response(422, 'Entidad improcesable', Respuesta_model_error)
    @api.expect(login_doc)
    def post(self):
        try:
            
            # Validación de la información
            login = Login_schema()
            usuario_login = login.load(request.json)

            # Consultamos qu el usuario exista, sino no hay login
            # select * from usuario where usuario.id == usuario.id
            usuario_db = db.session.execute(db.select(Usuario_model_db)
                                           .where(Usuario_model_db.correo == usuario_login['correo'])
                                           ).scalar_one()

            # Comparamos la contraseña
            if bcrypt.checkpw(usuario_login['password'].encode('utf-8'), usuario_db.password.encode('utf-8')):

                # La contraseña coincide
                usuario_db.ultimo_acceso = datetime.datetime.now()
                db.session.commit()

                usuario_schema = Usuario_schema(exclude=['password']).dump(usuario_db)

                # Retornamos el token
                access_token = create_access_token(identity=usuario_schema, expires_delta=datetime.timedelta(days=1))
                result = {
                    'token':access_token
                }

                return result, 200

            else:
                return {'message':'La contraseña no coincide'}, 404

        except NoResultFound:
            return {'message':'El correo no existe'}, 404
        except ValidationError as err:
            mensaje = ' '.join([f'{clave}: {" "}.join(mensajes)' for clave, mensaje in err.messages_dict.items()])
            return {'message': mensaje}, 422
        except Exception as err:
            return {'message': 'Algo salió mal, intentalo más tarde T-T'}, 503