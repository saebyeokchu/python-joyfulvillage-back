# 🏡 python-joyfulvillage-back — Backend for JoyfulVillage

**python-joyfulvillage-back** is the backend server for [JoyfulVillage](https://joyfulvillage.co.kr), a user-powered platform that allows anyone to upload, manage, and explore accommodations in serene, village-style communities.

Built with **Python Django**, this backend provides secure APIs, handles user-authenticated listings, image uploads, and acts as the backbone for all dynamic features seen in the JoyfulVillage frontend.

---

## 🔧 Features

- 🏠 User-generated accommodation listings
- 🔐 JWT-based authentication and user account management
- 🖼️ Room details and image upload support
- 📦 RESTful API built with Django REST Framework (DRF)
- 📆 Designed to support availability, filters, and location-based search
- 🌍 CORS-ready for seamless integration with the [TypeScript-based frontend](https://github.com/saebyeokchu/typescript-joyful-front)

---

## ⚙️ Tech Stack

| Layer             | Tech                         |
|------------------|------------------------------|
| Framework        | Django 4.x                   |
| API              | Django REST Framework (DRF)  |
| Auth             | JWT / Token-based auth       |
| Media Upload     | Django media handling        |
| Database         | SQLite (dev) / PostgreSQL (prod) |
| Deployment       | AWS EC2, Lightsail, etc.     |

---

## 📁 Project Structure

```bash
python-joyfulvillage-back/
├── village/                # Core Django app (rooms, users, API logic)
├── back/                   # Django project settings and URLs
├── media/                  # Uploaded user images
├── requirements.txt        # Python package dependencies
├── manage.py
└── README.md
```

---

## 🔐 Environment Setup

Use `.env` or system variables (via `python-decouple` or `os.environ`) to configure secrets:

```env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1

# Media settings
MEDIA_URL=/media/
MEDIA_ROOT=media/
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/saebyeokchu/python-joyfulvillage-back.git
cd python-joyfulvillage-back
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Migrations and Start Server

```bash
python manage.py migrate
python manage.py runserver
```

> Access the API locally at: `http://localhost:8000/api/`

---

## 📡 API Endpoints (Examples)

| Method | Endpoint           | Description                            |
|--------|--------------------|----------------------------------------|
| GET    | `/api/rooms/`      | List all accommodations                |
| POST   | `/api/rooms/`      | Create a new room listing              |
| POST   | `/api/upload/`     | Upload image or thumbnail              |
| POST   | `/api/register/`   | User registration                      |
| POST   | `/api/login/`      | User authentication                    |
| GET    | `/api/user/rooms/` | Get rooms uploaded by the current user |

---

## 🧩 Integrations

This backend works seamlessly with the React/Next.js frontend:

🔗 [`typescript-joyful-front`](https://github.com/saebyeokchu/typescript-joyful-front)

Make sure to enable CORS and use JWT in headers for authorized actions.

---

## 📦 Planned Enhancements

- [ ] Availability calendar integration
- [ ] Review and rating system
- [ ] Host/guest dashboards
- [ ] Admin approval for public listings
- [ ] Notification support (email/SMS)

---

## 🙌 Contributing

Have an idea or improvement? Pull requests and issues are welcome.  
Let’s build joyful online villages together.

---

## 📄 License

MIT License

---

Developed by [@saebyeokchu](https://github.com/saebyeokchu)  
Backend engine of **JoyfulVillage** 🏘️ — where hospitality meets community.
```

---
