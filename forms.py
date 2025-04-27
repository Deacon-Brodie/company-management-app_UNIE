from flask_wtf import FlaskForm

class DummyForm(FlaskForm):
    """Solo para validar CSRF automáticamente."""
    pass
