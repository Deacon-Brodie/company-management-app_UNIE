from flask import request, redirect, render_template, session
from server import app
from db import get_users_connection, hash_password
from forms import DummyForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = DummyForm()

    if 'username' in session:
        return redirect('/companies')

    if request.method == 'POST':
        if not form.validate_on_submit():
            return "Invalid CSRF token", 400

        username = request.form['username']
        password = request.form['password']
        conn = get_users_connection()
        user = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hash_password(password))).fetchone()
        conn.close()

        if user:
            session['username'] = user['username']
            session['role'] = user['role']
            session['company_id'] = user['company_id']
            return redirect('/companies')
        else:
            return render_template('auth/login.html', error="Invalid username or password")
    return render_template('auth/login.html')