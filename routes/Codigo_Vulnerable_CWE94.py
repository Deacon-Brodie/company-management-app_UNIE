from flask import request, Flask
app = Flask(__name__)

@app.route("/test")
def test():
    user_input = request.args.get("input")
    
    # VULNERABILIDAD: Ejecuta código arbitrario del usuario
    result = eval(user_input)
    return str(result)
