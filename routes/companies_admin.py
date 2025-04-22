from flask import request, redirect, render_template, session
from server import app
from db import get_data_connection

@app.route('/admin/companies')
def admin_list_companies():
    if session.get('role') != 'admin':
        return "Access denied", 403
    conn = get_data_connection()
    companies = conn.execute("SELECT * FROM companies").fetchall()
    conn.close()
    return render_template('admin/admin_companies.html', companies=companies)

@app.route('/admin/companies/add', methods=['GET', 'POST'])
def admin_add_company():
    if session.get('role') != 'admin':
        return "Access denied", 403
    if request.method == 'POST':
        company_name = request.form['company_name']
        owner = request.form['owner']
        conn = get_data_connection()
        conn.execute("INSERT INTO companies (name, owner) VALUES ('"+ company_name+"', '"+owner+"')")
        conn.commit()
        conn.close()
        return redirect('/admin/companies')
    return render_template('admin/admin_companies.html')

@app.route('/admin/companies/delete', methods=['POST'])
def delete_company():
    if session.get('role') != 'admin':
        return "Access denied", 403
    company = request.form['company']
    conn = get_data_connection()
    conn.execute("DELETE FROM companies WHERE id = "+ company)
    conn.execute("DELETE FROM comments WHERE company_id = " + company)
    conn.commit()
    conn.close()
    return redirect('/admin/companies')