from flask import Flask
from flask_restx import Resource, Api
from src.common.utils import api, db, ma, jwt
from flask_cors import CORS
import os
from src.routes.routes import Routes

# Crear una aplicacion
app = Flask(__name__)
CORS(app)

# Variable para controlar la documentacion
doc_visible = False

# La configuracion cambia
if os.environ['FLASK_ENV'] == 'development':
    app.config.from_object('settings.developer_config')
    doc_visible = True
elif os.environ['FLASK_ENV'] == 'production':
    app.config.from_object('settings.production_config')
else:
    app.config.from_object('settings.testing_config')

# Iniciar el objeto de la api
api.init_app(app)
api._doc = doc_visible
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)

# Punto de rutas principal
Routes(api)