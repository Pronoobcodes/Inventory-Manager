# 📦 Inventory Manager

A Django-based inventory management system where users can register, log in, and manage their product inventory through a clean and organized interface.

> 💡 Inspired by tutorials from **NetNinja** and **Bek Brace** on YouTube.

## 🖥️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## ✨ Features

- 🔐 User authentication — register and log in securely
- 📋 Add, view, edit, and delete products (full CRUD)
- 📊 Products displayed in an organized, sortable table
- 📱 Fully responsive UI built with Bootstrap
- 💾 SQLite database for simple, file-based storage

## 📁 Project Structure

```
Inventory-Manager/
├── invApp/           # Django app — models, views, URLs, templates
├── invProject/       # Django project settings and configuration
├── manage.py         # Django management script
├── db.sqlite3        # SQLite database
├── README.md
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pronoobcodes/Inventory-Manager.git
   cd Inventory-Manager
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Django**
   ```bash
   pip install django
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000`, register an account, and start managing your inventory!

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## Thanks to NetNinja and Bek Brace
This project was heavily inspired by and based on tutorials from the NetNinja YouTube and Bek Brace's channels. The tutorials provided excellent guidance in building Django apps and implementing user authentication and CRUD operations.
