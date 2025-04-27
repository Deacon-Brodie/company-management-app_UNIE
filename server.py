import os
from dotenv import load_dotenv
from flask import Flask, session, redirect, url_for, flash
from flask_wtf import CSRFProtect

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

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

from flask import session, redirect, url_for, flash
from server import app  # Asegúrate de importar la instancia de Flask

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('login'))  # Asegúrate que tienes la ruta 'login'