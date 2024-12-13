from flask_restx import fields
from src.common.utils import api

Respuesta_model_error = api.model('Respuesta_model_error',{
    'message': fields.String(description='Describe el tipo de error ocurrido')
})