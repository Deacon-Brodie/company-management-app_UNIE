from flask import request, Flask
app = Flask(__name__)

@app.route("/test")
def test():
    user_input = request.args.get("input")

    #  Corrección segura (por ejemplo, limitar entrada a enteros)
    try:
        result = int(user_input) * 2
        return str(result)
    except (ValueError, TypeError):
        return "Entrada inválida", 400
