from src.common.utils import ma
from marshmallow import fields, validate
from src.models.profesor_model import Profesor_model_db

class Profesor_schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Profesor_model_db
        ordered = True
        load_instance = True
        include_fk = True

class Profesor_regla_schema(ma.Schema):


    id_profesor = fields.Int(
        required = True,
        error_messages ={'required': 'El id del profesor es requerido'},  
        validate = validate.Range(min=1, max=None,error='El valor mínimo es 1')
    )
    nombre = fields.Str(
        required=True,
        error_messages={'required': 'El campo es requerido'},
        validate=validate.Length(min=1, max=200, error='El tamaño de la cadena debe ser entre 1 y 200')

    )
    apellido = fields.Str(
        required=True,
        error_messages={'required': 'El campo es requerido'},
        validate=validate.Length(min=1, max=200, error='El tamaño de la cadena debe ser entre 1 y 200')        
    )
    registro = fields.Int(
        required=True,
        error_messages={'required': 'El registro del personal es requerido'},
        validate = validate.Range(min=1, max=None,error='El valor mínimo es 1')        
    )
    id_usuario = fields.Int(
        required=True,
        error_messages={'required': 'El id del usuario es requerido'},
        validate = validate.Range(min=1,error='El valor mínimo es 1')      
    )  