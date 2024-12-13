from flask_restx import Resource
from src.schemas.login_schema import Login_schema
from flask import request
from flask_jwt_extended import create_access_token
from src.common.utils import api
from src.documentation.error_doc import Respuesta_model_error
from src.documentation.login_doc import login_doc, login_token_doc
from marshmallow import ValidationError
import datetime

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

            # Consultamos qu eel usuario exista, sino no hay login

            # Comparamos la contraseña

            # Retornamos el token de acceso
            access_token = create_access_token(identity='', expires_delta=datetime.timedelta(days=1))
            result = {
                'token': access_token
            }

            return result, 200
        except ValidationError as err:
            mensaje = ' '.join([f'{clave}: {" "}.join(mensajes) for clave, mensaje in err.messages_dict.items()'])
            return {'message': mensaje}, 422
        except Exception as err:
            return {'message': 'Algo salió mal, intentalo más tarde T-T'}, 503