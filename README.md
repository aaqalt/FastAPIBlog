# FastAPI Blog Project

A **FastAPI**-based blog application featuring **user authentication**, **JWT token authorization**, and **CRUD operations** for blogs. Passwords are securely **encrypted and decrypted**, and blog data is stored in **PostgreSQL**.

---

## Features

- **User Authentication & Authorization**
  - JWT token-based login and registration
  - Secure password hashing

- **Blog Management**
  - Create, Read, Update, Delete (CRUD) blogs
  - Associate blogs with users (authors)

- **Database**
  - PostgreSQL integration
  - Persistent storage of users and blogs

- **Security**
  - Password encryption and decryption
  - JWT token verification for protected routes

---

## Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Authentication:** JWT tokens
- **Password Security:** Hashing (bcrypt)
- **ORM:** SQLAlchemy / Tortoise ORM (depending on implementation)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/fastapi-blog.git
   cd fastapi-blog
