# 📘 FastAPI Social Login (Google + Facebook) with JWT Authentication
## ❤️ Author

Created by **Bala⚡Selvam** using FastAPI + Authlib + Jinja2 + JWT.
#################################################################################

This project demonstrates a complete authentication flow using **FastAPI**, **Jinja2 templates**, **Authlib OAuth**, and **JWT tokens**.

It supports:

- 🔵 **Google SSO**
- 🔷 **Facebook SSO**
- 🟡 **JWT Token Generation**
- 🎨 A clean sky-blue login UI
- 🍪 JWT stored as HttpOnly cookie
- 🔐 Session-based OAuth state storage

---

## 🚀 Features

- ✔ FastAPI backend  
- ✔ Google & Facebook OAuth login  
- ✔ Jinja2 template rendering  
- ✔ JWT access tokens  
- ✔ Session middleware  
- ✔ Clean login UI  
- ✔ Logout support  
- ✔ Fully configurable via `.env`  

---

## 📂 Project Structure

```
.
├── main.py
├── auth.py
├── templates/
│   ├── login.html
│   └── home.html
├── .env
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
py -3.11 -m venv ssoenv
ssoenv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn authlib python-dotenv jinja2 httpx itsdangerous PyJWT python-multipart requests
```

Or use the `requirements.txt`.

### 3️⃣ Create `.env` File

```
# ===== GOOGLE SSO =====
GOOGLE_CLIENT_ID=YOUR_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET=YOUR_GOOGLE_CLIENT_SECRET
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/callback/google

# ===== FACEBOOK SSO =====
FACEBOOK_CLIENT_ID=YOUR_FACEBOOK_APP_ID
FACEBOOK_CLIENT_SECRET=YOUR_FACEBOOK_APP_SECRET
FACEBOOK_REDIRECT_URI=http://localhost:8000/auth/callback/facebook

# ===== SESSION & JWT =====
SESSION_SECRET=super-secret-session-key
JWT_SECRET=your-jwt-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=30
```

---

## 🎯 Google Setup Steps

- Go to: [Google Cloud Console](https://console.cloud.google.com)
- API & Services → Credentials
- Create **OAuth Client ID (Web)**
- Add redirect URI:  
  `http://localhost:8000/auth/callback/google`
- Copy Client ID and Client Secret to `.env`

---

## 🔷 Facebook Setup Steps

- Visit: [Facebook Developers](https://developers.facebook.com/)
- Create App → Consumer
- Add Product → Facebook Login → Web
- Add Valid OAuth Redirect URI:  
  `http://localhost:8000/auth/callback/facebook`
- Copy App ID and App Secret to `.env`
- Switch App to Live Mode to allow email scope

---

## 🧠 Generate JWT After SSO

After successful Google/Facebook login, your `main.py` callback will:

1. Extract user info
2. Generate a JWT token
3. Send token inside an HttpOnly cookie
4. Render home page with user data

---

## ▶ Run the Application

```bash
uvicorn main:app --reload
```

Visit: [http://localhost:8000/](http://localhost:8000/)

---

### 🔐 Logout

[http://localhost:8000/logout](http://localhost:8000/logout)

This will:

- Clear OAuth session
- Remove JWT cookie
- Redirect to login page

---

## 🖥 Login UI Preview

- ✔ Clean sky-blue theme
- ✔ Google & Facebook buttons
- ✔ Responsive design

Login page file: `templates/login.html`

---

## 🛡 Security Notes

- JWT cookie is HttpOnly to prevent XSS
- Use HTTPS for secure cookies
- Update `SESSION_SECRET` & `JWT_SECRET` in production
- Use environment variables (never commit secrets)

---

## 📌 Next Enhancements (Optional)

You can easily extend this project to include:

- 🔐 Protected API routes that require JWT
- 🗄️ Storing users in DB (PostgreSQL / DynamoDB)
- 🔄 Refresh token support
- 🏢 Azure AD SSO (Office 365 Login)
- 🎨 Frontend React/Angular integration

