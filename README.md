
# Company Management App

**Company Management App** is a web platform that allows users to manage companies and post comments about them. The application supports three roles (`admin`, `owner`, and `user`) with different permissions and access levels.

This system simulates a realistic business environment and includes features such as user authentication, role-based access control, and dynamic forms. It uses Bootstrap for a responsive interface and intentionally includes common security vulnerabilities for educational purposes.

---

## 🚀 Features

- User authentication with role-based access
- Company listing, creation, editing, and viewing
- Commenting system
- Admin dashboard for user and company management
- Toast notifications and dynamic form behavior

---

## 🧱 Technologies Used

- **Python 3** with **Flask**
- **SQLite** for database
- **Bootstrap 5** for responsive UI
- **Jinja2** for templating
- **JavaScript** for interactivity

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-org/company-management-app.git
cd company-management-app
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
python main.py
```

✅ The database will be automatically initialized on the first run.

4. Visit: `http://127.0.0.1:5000`

---

## 📂 Project Structure

```
.
├── main.py                 # Entry point to run the Flask app
├── server.py               # Flask app instance
├── db/
│   └── __init__.py         # Initializes SQLite databases
├── routes/
│   ├── auth.py             # Login/logout routes
│   ├── companies.py        # Routes for company views and comments
│   └── users_admin.py      # Admin-only user management
├── templates/
│   ├── base.html           # Shared HTML layout
│   ├── auth/               # Login page
│   ├── companies/          # Pages for listing and managing companies
│   └── admin/              # Admin dashboard templates
├── static/
│   └── css/style.css       # Custom styles
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── LICENSE                 # License file
```

---

## 🌐 Application Routes

| Route                    | Description                             | Access Level           |
|--------------------------|-----------------------------------------|------------------------|
| `/`                      | Redirects to login page                 | Public                 |
| `/login`                 | User login                              | Public                 |
| `/logout`                | Logout current session                  | Logged-in users        |
| `/admin/users`           | User management panel                   | Admin only             |
| `/admin/companies`       | View list of all companies              | Admin only             |
| `/admin/companies/add`   | Add new company                         | Admin only             |
| `/admin/companies/delete`| Delete a company                        | Admin only             |

➡️ Additional routes (such as for owners and company pages) may be dynamically registered or located in other parts of the application depending on role and logic.

---

## 🧪 Default Users

| Username | Password   | Role   | Notes                      |
|----------|------------|--------|----------------------------|
| `alice`  | password1  | user   | Can post comments          |
| `bob`    | password2  | owner  | Owns "Insegura Corp"       |
| `admin`  | admin123   | admin  | Full access                |

---

