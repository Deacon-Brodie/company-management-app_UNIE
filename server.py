from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Clave segura necesaria para CSRF y sesiones
app.permanent_session_lifetime = 99999999

csrf = CSRFProtect(app)  # Activar protección CSRF

# Configuración segura de cookies
app.config.update(
    SESSION_COOKIE_SECURE=True,
    WTF_CSRF_ENABLED=True,  # Activar explícitamente CSRF
    WTF_CSRF_SECRET_KEY='otra-super-clave-secreta-para-csrf',  # Clave específica para firmar CSRF tokens
)

# Corregido: Inyectar csrf_token directamente
@app.context_processor
def inject_csrf_token():
    from flask_wtf.csrf import generate_csrf
    return dict(csrf_token=generate_csrf())

# Importar rutas al final para evitar errores de importación circular
from routes import companies_admin, users_admin, auth