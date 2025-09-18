# 📝 Task Manager API  

A RESTful API for managing personal tasks, built with **Django Rest Framework (DRF)** and **JWT authentication**.  
This API allows users to register, authenticate, and manage their tasks with filtering, priority levels, and overdue detection.  

---

## 🚀 Features  

- **User Authentication**
  - JWT-based login and token authentication.
  - User registration endpoint with password hashing.
  
- **Task Management**
  - Create, retrieve, update, and delete tasks.
  - Each task belongs to a specific user.
  - Priority levels (1 = Low, 2 = Medium, 3 = High).
  - Task completion and archival support.

- **Filtering**
  - Filter tasks by:
    - `completed` status
    - `priority`
    - `overdue` (tasks past their due date and not completed).

- **Permissions**
  - Only authenticated users can access task endpoints.
  - Registration is limited to `POST` requests only.

---

## 📦 Tech Stack  

- **Backend:** Django, Django Rest Framework  
- **Authentication:** JWT (via `djangorestframework-simplejwt`)  
- **Filtering:** django-filter  
- **Database:** SQLite (default) or configurable to Postgres/MySQL  

---

## ⚙️ Installation & Setup  

```bash
git clone https://github.com/your-username/taskmanagerapi.git
cd taskmanagerapi

# create virtual environment
python -m venv venv
source venv/bin/activate   # (on Windows: venv\Scripts\activate)

# install dependencies
pip install -r requirements.txt

# run migrations
python manage.py migrate

# run the server
python manage.py runserver
