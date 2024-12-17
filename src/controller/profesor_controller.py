from flask_restx import Resource
from src.schemas.profesor_schema import Profesor_schema, Profesor_regla_schema
from src.models.profesor_model import Profesor_model_db
from src.documentation.profesor_doc import Profesor_doc, Profesor_create_doc
from src.documentation.error_doc import Respuesta_model_error
from flask import request
from src.common.utils import db, api
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound

class Profesor_controller(Resource):

    @api.doc(description='Permite crear profesores del sistema')
    @api.response(201, 'Éxito, Profesor creado', Profesor_doc)
    @api.response(401, 'Acceso no autorizado')
    @api.response(422, 'Entidad improcesable', Respuesta_model_error)
    @api.response(503, 'Ocurrio un problema en el sistema', Respuesta_model_error)
    @api.expect(Profesor_create_doc)    
    def post(self):
        try:
            # Usuario actual
            # current_user = get_jwt_identity()

            # Validar las reglas
            profesor_schema = Profesor_regla_schema(exclude=['id_profesor']).load(request.json)

            profesor = Profesor_schema(exclude=['id_profesor']).load(request.json)
            # profesor.id_usuario = current_user['id_usuario']
            
            # Inserción
            db.session.add(profesor)
            db.session.commit()
            return Profesor_schema().dump(profesor), 201
        except IntegrityError:
            return {'message': 'El registro de personal ya existe para profesor'}, 406
        except ValidationError as err:
            mensaje = ' '.join([f'{clave}: {" ".join(mensaje)}' for clave, mensaje in err.messages_dict.items()])
            return {'message': mensaje}, 422
        except Exception as err:    
            return {'message': 'Algo salio mal'}, 503 



    @api.doc(description='Permite crear profesores del sistema')
    @api.response(200, 'Éxito, Profesor creado', [Profesor_doc])
    @api.response(401, 'Acceso no autorizado')
    @api.response(503, 'Ocurrio un problema en el sistema', Respuesta_model_error) 
    def get(self):
        try:
            profesores = db.session.execute(db.select(Profesor_model_db)).scalars().all()

            return Profesor_schema(many=True).dump(profesores), 200
        except Exception as err:
            return {'message': 'Algo salió mal, intentalo más tarde T-T'}, 503     


class Profesor_by_id_controller(Resource):

    @api.doc(description='Permite crear profesores del sistema')
    @api.response(201, 'Éxito, Profesor creado', Profesor_doc)
    @api.response(401, 'Acceso no autorizado')
    @api.response(404, 'El profesor a eliminar no existe', Respuesta_model_error)
    @api.response(503, 'Ocurrio un problema en el sistema', Respuesta_model_error) 
    def delete(self, id_profesor):
        try:
            profesor = db.session.execute(db.select(Profesor_model_db).where(Profesor_model_db.id_profesor == id_profesor)).scalar_one()

            db.session.delete(profesor)
            db.session.commit()

            return True, 200

        except NoResultFound:
            return {'message':'El profesor que intentas eliminar no existe'}, 404
        except Exception as err:
            return {'message': 'Algo salió mal, intentalo más tarde T-T'}, 503       