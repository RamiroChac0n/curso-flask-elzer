from flask_restx import Namespace
from src.controller.profesor_controller import Profesor_controller, Profesor_by_id_controller
from src.common.utils import api

def Profesor_routes(api):
    ns_profesor = Namespace(name='profesor', description='Describe los puntos de acceso de profesor')

    # Expone las rutas
    ns_profesor.add_resource(Profesor_controller, '')
    ns_profesor.add_resource(Profesor_by_id_controller, '/id_profesor/<int:id_profesor>')

    api.add_namespace(ns_profesor)