from flask import request, redirect, render_template, session
from server import app
from db import get_data_connection
from forms import DummyForm

@app.route('/admin/companies')
def admin_list_companies():
    if session.get('role') != 'admin':
        return "Access denied", 403

    conn = get_data_connection()
    companies = conn.execute("SELECT * FROM companies").fetchall()
    conn.close()
    return render_template('admin/admin_companies.html', companies=companies)

@app.route('/admin/companies/add', methods=['POST'])
def admin_add_company():
    form = DummyForm()
    if not form.validate_on_submit():
        return "Invalid CSRF token", 400

    if session.get('role') != 'admin':
        return "Access denied", 403

    company_name = request.form['company_name']
    owner = request.form['owner']
    conn = get_data_connection()
    conn.execute("INSERT INTO companies (name, owner) VALUES (?, ?)", (company_name, owner))
    conn.commit()
    conn.close()
    return redirect('/admin/companies')

@app.route('/admin/companies/delete', methods=['POST'])
def delete_company():
    form = DummyForm()
    if not form.validate_on_submit():
        return "Invalid CSRF token", 400

    if session.get('role') != 'admin':
        return "Access denied", 403

    company_id = request.form['company']
    conn = get_data_connection()
    conn.execute("DELETE FROM companies WHERE id = ?", (company_id,))
    conn.commit()
    conn.close()
    return redirect('/admin/companies')
