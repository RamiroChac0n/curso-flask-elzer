from src.common.utils import ma
from src.models.usuario_model import Usuario_model_db # OJO ACÁ
from marshmallow import fields, validate

class Usuario_schema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario_model_db
        ordered = True
        load_instance = True
        include_fk = True

class Usuario_regla_schema(ma.Schema):


    id_usuario = fields.Int(
        required = True,
        error_messages ={'required': 'El id del usuario es requerido'},  
        validate = validate.Range(min=1, max=None,error='El valor mínimo es 1')
    )
    nombre = fields.Str(
        required=True,
        error_messages={'required': 'El campo es requerido'},
        validate=validate.Length(min=1, max=200, error='El tamaño de la cadena debe ser entre 1 y 200')

    )
    correo = fields.Str(
        required=True,
        error_messages={'required': 'El campo es requerido'},
        validate=validate.Length(min=1, max=200, error='El tamaño de la cadena debe ser entre 1 y 200')        
    )
    password = fields.Str(
        required=True,
        error_messages={'required': 'El campo es requerido'},
        validate=validate.Length(min=1, max=200, error='El tamaño de la cadena debe ser entre 1 y 200')        
    )
    ultimo_acceso = fields.Str(
        required=True,
        error_messages={'required': 'El campo es requerido'}      
    )
    id_rol = fields.Int(
        required=True,
        error_messages={'required': 'El id del rol es requerido'},
        validate = validate.Range(min=1,error='El valor mínimo es 1')
    )   