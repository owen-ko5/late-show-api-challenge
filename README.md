# 🎬 LATE SHOW API

A RESTful API for managing guests, episodes, and appearances on the *Late Show*! Built with Flask, SQLAlchemy, JWT Authentication, and PostgreSQL.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-%23000?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23336791?logo=postgresql)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📚 TABLE OF CONTENT

- [📦 Features](#-features)
- [⚙️ Setup](#️-setup)
- [📂 Project Structure](#-project-structure)
- [🔐 Authentication](#-authentication)
- [🚀 API Endpoints](#-api-endpoints)
- [🧪 Running Tests](#-running-tests)
- [📌 License](#-license)

---

## 📦 FEATURES

- User registration and login with JWT authentication 🔐
- Create, list, and delete TV episodes 📺
- Add and view guests and their appearances 👤
- Rate guest appearances with a 1-5 scale ⭐
- PostgreSQL database integration 🐘

---

## ⚙️ SETUP

> 🛠️ Requires Python 3.8+, PostgreSQL, and pip.

```bash
# Clone the repository
git clone https://github.com/your-username/late-show-api.git
cd late-show-api

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

## Install dependencies
pip install -r requirements.txt

# Setup PostgreSQL database
# Ensure PostgreSQL is running and replace credentials if needed
psql -U postgres
CREATE DATABASE late_show_api_dev;
\q

# Configure environment
export FLASK_APP=server/app.py
 export FLASK_APP=server.app:create_app

# Run migrations
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Optional: Seed the database
python server/seed.py

# Start the development server
flask run

## PROJECT STRUCTURE
late-show-api/
├── server/
│   ├── app.py
│   ├── config.py
│   ├── seed.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── guest.py
│   │   ├── episode.py
│   │   ├── appearance.py
│   ├── controllers/
│   │   ├── auth_controller.py
│   │   ├── guest_controller.py
│   │   ├── episode_controller.py
│   │   ├── appearance_controller.py
├── migrations/
├── requirements.txt
└── README.md

## 🔐 AUTHENTICATION
This API uses JWT (JSON Web Token) for securing endpoints.

Register: POST /auth/register

Login: POST /auth/login

Protected routes require Authorization: Bearer <token>

##🚀 API ENDPOINTS
🧑 Users
Method	Endpoint	Description
POST	/auth/register	Register a new user
POST	/auth/login	Login and get token

👤 Guests
Method	Endpoint	Description
GET	/guests	List all guests

📺 Episodes
Method	Endpoint	Description
GET	/episodes	List all episodes
GET	/episodes/<id>	Retrieve episode detail
DELETE	/episodes/<id>	Delete episode (auth)


##🌟 APPEARANCES
Method	Endpoint	Description
POST	/appearances	Add a guest appearance (auth)

{
  "guest_id": 1,
  "episode_id": 2,
  "rating": 5
}

##📌 LICENSE
This project is licensed under the MIT License. See LICENSE for details.

##🧑‍💻 AUTHOR
Made with ❤️ by Marciah Ayora

##💡 FUTURE IDEAS
Admin dashboard

Search + filter episodes by guest

CSV/Excel export of appearances# -Flask-Code-Challenge-Late-Show-API
