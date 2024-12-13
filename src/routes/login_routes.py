from flask_restx import Namespace
from src.controller.login_controller import Login_controller
from src.common.utils import api

def Login_routes(api):
    ns_login = Namespace(name='login', description='Describe los puntos de acceso a la api')

    # Expone las rutas
    ns_login.add_resource(Login_controller, '')

    api.add_namespace(ns_login)