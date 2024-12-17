from src.routes.login_routes import Login_routes
from src.routes.usuario_routes import Usuario_routes
from src.routes.profesor_routes import Profesor_routes

def Routes(api):
    # Rutas para login
    Login_routes(api)

    # Rutas para usuario
    Usuario_routes(api)

    # Rutas para profesor
    Profesor_routes(api)