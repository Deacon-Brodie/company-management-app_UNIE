from db import get_users_connection, hash_password
from flask import request, redirect, render_template, session, flash
from server import app
import sqlite3

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect('/companies')

    if request.method == 'POST':
        # Validación básica de entrada
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash("Username and password are required.")
            return render_template('auth/login.html')

        try:
            conn = get_users_connection()
            cursor = conn.cursor()
            # Consulta segura parametrizada
            cursor.execute(
                "SELECT * FROM users WHERE username = ? AND password = ?",
                (username, hash_password(password))
            )
            user = cursor.fetchone()
        except sqlite3.Error:
            # No exponer errores internos
            flash("Something went wrong. Please try again.")
            user = None
        finally:
            conn.close()

        if user:
            # Establece la sesión
            session['username'] = user['username']
            session['role'] = user['role']
            session['company_id'] = user['company_id']
            return redirect('/companies')
        else:
            # Mensaje genérico
            flash("Invalid credentials.")
            return render_template('auth/login.html')

    return render_template('auth/login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')