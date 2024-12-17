from marshmallow import Schema, fields

class Login_schema(Schema):
    correo = fields.Str(
        required=True,
        error_messages={'required': 'El correo es obligatorio'}
    )
    password = fields.Str(
        required=True,
        error_messages={'required': 'La contraseña es obligatoria'}
    )