# 🩸 Blood Bank Inventory Management System

A web-based **Blood Bank Inventory Management System** developed using **Django**, **MySQL**, **HTML**, and **CSS**. The application enables efficient management of blood donor records through a simple and user-friendly interface while performing complete CRUD (Create, Read, Update, Delete) operations.

## 📖 Overview

The Blood Bank Inventory Management System is designed to simplify the process of maintaining donor information. Users can register new donors, view existing records, update donor details, and delete records whenever required. All information is securely stored in a MySQL database and synchronized automatically with the application.
This project demonstrates full-stack web development using Django, database integration with MySQL, form handling, data validation, and CRUD functionality.
## ✨ Features

* 📝 Donor registration form
* 👤 Store donor details such as:

  * Name
  * Age
  * Date of Birth
  * Blood Group
  * Disease History
  * Parents' Blood Groups
* 💾 Secure storage using MySQL
* 📋 View all registered donor records
* ✏️ Edit and update donor information
* 🗑️ Delete donor records
* 🔄 Automatic database synchronization for all CRUD operations
* 🎨 Responsive user interface built with HTML and CSS

## 🛠️ Tech Stack

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Programming Language |
| Django     | Backend Framework    |
| MySQL      | Database             |
| HTML       | Frontend Structure   |
| CSS        | Styling              |

## 🚀 Getting Started
### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/blood_bank_inventory.git
```

### 2. Navigate to the Project Folder

```bash
cd blood_bank_inventory
```

### 3. Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL

* Create a MySQL database.
* Update the database credentials in `settings.py`.

Example:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "your_database_name",
        "USER": "your_username",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

### 8. Open the Application

Visit:

```
http://127.0.0.1:8000/
```

## 📚 Learning Outcomes

This project demonstrates:

* Django project structure
* CRUD operations
* Form handling and validation
* MySQL database integration
* Backend development with Django
* Frontend development using HTML and CSS
* Database connectivity and synchronization

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

## 📄 License

This project is developed for educational and learning purposes.

## 👩‍💻 Author

**Yashita Gupta**
GitHub: https://github.com/Yashitag11
