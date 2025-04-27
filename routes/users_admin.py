from flask import request, redirect, render_template, session
from server import app
from db import get_users_connection, get_data_connection, hash_password
from forms import DummyForm

@app.route('/admin/users')
def admin_users():
    if session.get('role') != 'admin':
        return "Access denied", 403

    conn_u = get_users_connection()
    users = conn_u.execute("SELECT * FROM users").fetchall()
    conn_u.close()

    conn_d = get_data_connection()
    companies = conn_d.execute("SELECT * FROM companies").fetchall()
    conn_d.close()

    return render_template('admin/admin_users.html', users=users, companies=companies)

@app.route('/admin/users/add', methods=['POST'])
def add_user():
    form = DummyForm()
    if not form.validate_on_submit():
        return "Invalid CSRF token", 400

    if session.get('role') != 'admin':
        return "Access denied", 403

    username = request.form['username']
    password = request.form['password']
    role = request.form['role']
    company_id = request.form.get('company_id') if role == 'owner' else None

    conn = get_users_connection()
    if company_id:
        conn.execute("INSERT INTO users (username, password, role, company_id) VALUES (?, ?, ?, ?)", (username, hash_password(password), role, company_id))
    else:
        conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hash_password(password), role))
    conn.commit()
    conn.close()
    return redirect('/admin/users')
