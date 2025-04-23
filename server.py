from flask import Flask

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.permanent_session_lifetime = 99999999

# Configuración segura centralizada, donde declaramos el uso de SECURE, debido a que HttpOnly esta activado por defecto.
app.config.update(
    SESSION_COOKIE_SECURE=True,
)