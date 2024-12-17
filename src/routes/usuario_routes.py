from flask_restx import Namespace
from src.controller.usuario_controller import Usuario_controller
from src.common.utils import api

def Usuario_routes(api):
    ns_usuario = Namespace(name='usuario', description='Describe los endpoinst para usuario')

    # Expone las rutas
    ns_usuario.add_resource(Usuario_controller, '')

    api.add_namespace(ns_usuario)