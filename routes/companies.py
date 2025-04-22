from flask import request, redirect, render_template, session
from server import app
from db import get_data_connection

@app.route('/')
def index():
    return redirect('/login')

@app.route('/companies')
def list_companies():
    if 'username' not in session:
        return redirect('/login')
    conn = get_data_connection()
    companies = conn.execute("SELECT * FROM companies").fetchall()

    # Agregar el número de comentarios para cada empresa
    companies_list = []
    for company in companies:
        company_dict = dict(company)  # Convertir la fila a un diccionario
        company_dict['comment_count'] = conn.execute("SELECT COUNT(*) FROM comments WHERE company_id = ?", (company_dict['id'],)).fetchone()[0]
        companies_list.append(company_dict)
    
    conn.close()
    return render_template('companies/home.html', companies=companies_list)



@app.route('/companies/<int:company_id>', methods=['GET', 'POST'])
def company_detail(company_id):
    if 'username' not in session:
        return redirect('/login')
    conn = get_data_connection()
    company = conn.execute("SELECT * FROM companies WHERE id = " + str(company_id)).fetchone()
    comments = conn.execute("SELECT * FROM comments WHERE company_id = " + str(company_id)).fetchall()
    if request.method == 'POST':
        comment = request.form['comment']
        user = session.get('username')
        conn.execute("INSERT INTO comments (company_id, user, comment) VALUES ("+str(company_id)+", '"+user+"', '"+comment+"')")
        conn.commit()
        conn.close()
        return redirect('/companies/'+str(company_id))
    conn.close()
    if not company:
        return "Company not found", 404
    return render_template('companies/company.html', company=company, comments=comments)

@app.route('/companies/register', methods=['GET', 'POST'])
def register_company():
    if session.get('role') != 'owner':
        return "Access denied", 403
    if request.method == 'POST':
        company_name = request.form['company_name']
        description = request.form['description']
        owner = session.get('username')
        conn = get_data_connection()
        conn.execute("INSERT INTO companies (name, description, owner) VALUES ("+company_name+", '"+description+"', '"+owner+"')")
        conn.commit()
        conn.close()
        return redirect('/companies')
    return render_template('companies/register_company.html')


@app.route('/companies/<int:company_id>/edit', methods=['GET', 'POST'])
def edit_company(company_id):
    if 'username' not in session:
        return redirect('/')
    conn = get_data_connection()
    company = conn.execute("SELECT * FROM companies WHERE id = "+ str(company_id)).fetchone()
    if not company:
        conn.close()
        return "Company not found", 404
    if session.get('role') != 'admin' and session.get('username') != company['owner']:
        conn.close()
        return "Access denied", 403
    if request.method == 'POST':
        new_name = request.form['company_name']
        new_description = request.form['description']
        conn.execute("UPDATE companies SET name = '"+new_name+"', description = '"+new_description+"' WHERE id = "+str(company_id))
        conn.commit()
        conn.close()
        return redirect('/companies')
    conn.close()
    return render_template('companies/edit_company.html', company=company)


