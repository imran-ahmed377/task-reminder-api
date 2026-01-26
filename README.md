# Student Task & Reminder API

A complete, production-ready full-stack web application for managing student tasks and reminders.

**🎯 Status**: Frontend Complete ✅ | Ready for Azure Deployment 🚀

---

## 📖 Table of Contents

1. [Quick Start](#-quick-start)
2. [Project Overview](#-project-overview)
3. [Features](#-features)
4. [Architecture](#-architecture)
5. [File Structure](#-file-structure)
6. [API Documentation](#-api-documentation)
7. [Deployment](#-deployment)
8. [Learning Resources](#-learning-resources)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip (Python package manager)
- Modern web browser

### Installation

```bash
# 1. Navigate to project directory
cd "c:\Users\Asus\Desktop\Skills Upgrade\RestAPI"

# 2. Create virtual environment (optional but recommended)
python -m venv rest_api_env

# 3. Activate virtual environment
# Windows:
rest_api_env\Scripts\activate
# Mac/Linux:
source rest_api_env/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
# Start the API server
uvicorn main:app --reload --host 127.0.0.1 --port 8001
```

### Access the Application

Open your browser and navigate to:
```
http://localhost:8001
```

You'll see the Task Manager interface with:
- Registration form
- Login form
- Task management dashboard (after login)

---

## 📊 Project Overview

### What Is This?

A **full-stack web application** that demonstrates professional REST API design and web development concepts. Students can:

- Register and login securely
- Create, read, update, and delete (CRUD) tasks
- Mark tasks as complete
- Set due dates and descriptions
- Access from any modern browser

### Tech Stack

**Backend**
- Python 3.11
- FastAPI (modern web framework)
- SQLAlchemy (database ORM)
- SQLite (database)
- JWT (authentication)
- Bcrypt (password hashing)

**Frontend**
- HTML5
- CSS3
- Vanilla JavaScript (ES6+)
- No frameworks - pure, learnable code

**Deployment**
- Azure App Service
- Docker (optional)
- Gunicorn (production server)

### Time to Deploy

- ⏱️ 5 minutes to run locally
- ⏱️ 15 minutes to deploy to Azure

---

## ✨ Features

### Core Features

✅ **User Authentication**
- Secure registration with email
- JWT-based login
- Password hashing with bcrypt
- Session management with tokens

✅ **Task Management**
- Create tasks with title, description, due date
- List all tasks
- Edit existing tasks
- Mark tasks as complete
- Delete tasks

✅ **Responsive Design**
- Works on desktop, tablet, mobile
- Clean, modern UI
- Intuitive user experience
- Real-time feedback with alerts

✅ **Production Ready**
- Error handling
- Input validation
- CORS support
- Database persistence
- Comprehensive logging

### Advanced Features

🔐 **Security**
- Password hashing (bcrypt)
- JWT token validation
- CORS protection
- Input sanitization
- SQL injection prevention

📚 **Documentation**
- Swagger UI (interactive API docs)
- ReDoc (readable API docs)
- Comprehensive README
- Code comments throughout
- Usage guides

🧪 **Testing**
- Automated test suite
- Manual test guide
- Example requests
- Validation checks

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────────┐
│ Web Browser                                             │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ index.html - React-less Frontend                    │ │
│ │ • Registration/Login forms                          │ │
│ │ • Task dashboard                                    │ │
│ │ • Pure JavaScript + CSS                             │ │
│ └─────────────────────────────────────────────────────┘ │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP/JSON
                     │ (Bearer Token)
         ┌───────────▼───────────┐
         │   FastAPI Server      │
         │   (main.py)           │
         │ ┌─────────────────┐   │
         │ │ /              │   │ Serves Frontend
         │ │ /auth/*        │   │ User Management
         │ │ /tasks/*       │   │ Task CRUD
         │ │ /docs          │   │ API Documentation
         │ └─────────────────┘   │
         └───────────┬───────────┘
                     │ SQL Queries
         ┌───────────▼───────────┐
         │   SQLite Database     │
         │   (tasks.db)          │
         │ ┌─────────────────┐   │
         │ │ users table     │   │
         │ │ tasks table     │   │
         │ └─────────────────┘   │
         └───────────────────────┘
```

### Data Flow

1. **User opens browser** → Frontend HTML loaded
2. **User registers** → Credentials sent to API → Stored in database (password hashed)
3. **User logs in** → Credentials verified → JWT token issued
4. **User creates task** → Frontend sends task data + token → API validates token → Task stored
5. **User views tasks** → Frontend sends request + token → API returns user's tasks
6. **User updates task** → Frontend sends update + token → API updates database
7. **User deletes task** → Frontend sends delete + token → API removes from database

---

## 📁 File Structure

```
RestAPI/
│
├── 🌐 Frontend Files
│   └── index.html                 # Single-page web app (500+ lines)
│
├── 🔧 Python Backend
│   ├── main.py                    # FastAPI application entry point
│   ├── routes.py                  # Task endpoints (6 endpoints)
│   ├── auth_routes.py             # Authentication endpoints (register, login)
│   ├── database.py                # Database configuration & session
│   ├── db_models.py               # SQLAlchemy ORM models
│   ├── auth_db_models.py          # User database model
│   ├── models.py                  # Pydantic request/response schemas
│   ├── auth.py                    # JWT & password utilities
│   └── test_api.py                # Automated test suite
│
├── ⚙️ Configuration
│   ├── requirements.txt           # Python dependencies
│   ├── .env                       # Environment variables
│   └── .gitignore                # Git ignore rules
│
├── 📚 Documentation
│   ├── README.md                  # This file
│   ├── QUICKSTART.md              # Quick setup guide
│   ├── FRONTEND.md                # Frontend documentation
│   ├── TESTING.md                 # Testing guide
│   ├── DEPLOYMENT.md              # Azure deployment guide
│   ├── PROJECT_SUMMARY.md         # Project overview
│   └── TEST_RESULTS.md            # Test results summary
│
├── 💾 Runtime
│   ├── tasks.db                   # SQLite database (auto-created)
│   ├── __pycache__/               # Python cache (auto-generated)
│   └── rest_api_env/              # Virtual environment
│
└── 🐳 Deployment (Optional)
    ├── Dockerfile                 # Docker image definition
    └── docker-compose.yml         # Docker compose file
```

### File Descriptions

| File | Purpose | Key Code |
|------|---------|----------|
| `index.html` | Frontend UI | Form handling, API calls, localStorage |
| `main.py` | App setup | FastAPI creation, route mounting |
| `routes.py` | Task CRUD | POST, GET, PUT, PATCH, DELETE endpoints |
| `auth_routes.py` | User auth | Register, login, token validation |
| `models.py` | Data schemas | Request/response validation with Pydantic |
| `auth.py` | Security | JWT creation, password hashing |
| `database.py` | DB config | SQLAlchemy engine, session management |

---

## 🔌 API Documentation

### Interactive Documentation

Once running, visit:
- **Swagger UI**: `http://localhost:8001/docs` (interactive)
- **ReDoc**: `http://localhost:8001/redoc` (readable)

### Base URL

```
http://localhost:8001
```

### Authentication

All task endpoints require a JWT token in the Authorization header:

```
Authorization: Bearer <token>
```

Get a token by logging in:
```bash
POST /auth/login
Content-Type: application/json

{
  "username": "john_doe",
  "password": "password123"
}

Response:
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

### Endpoints

#### Authentication

```http
POST /auth/register
POST /auth/login
```

#### Tasks (Protected)

```http
GET    /tasks/              # List all tasks
POST   /tasks/              # Create task
GET    /tasks/{id}          # Get single task
PUT    /tasks/{id}          # Update task
PATCH  /tasks/{id}/complete # Mark complete
DELETE /tasks/{id}          # Delete task
```

#### Utility

```http
GET /              # Serves frontend
GET /api/health    # Health check
GET /docs          # Swagger UI
GET /redoc         # ReDoc
```

### Example Requests

See `TESTING.md` for detailed examples with cURL and PowerShell.

---

## 🚀 Deployment

### Local Development

```bash
# Start server
uvicorn main:app --reload --host 127.0.0.1 --port 8001

# Open browser
http://localhost:8001
```

### Azure Deployment

1. **Create Azure Account**: https://azure.microsoft.com/free/
2. **Deploy Application**: See `DEPLOYMENT.md` for detailed steps
3. **Access Online**: `https://your-app-name.azurewebsites.net`

### Docker Deployment (Optional)

```bash
# Build image
docker build -t student-task-api .

# Run container
docker run -p 8001:8000 student-task-api

# Access
http://localhost:8001
```

---

## 📚 Learning Resources

### What You'll Learn

This project teaches:

**REST API Design**
- Proper endpoint naming conventions
- HTTP methods (GET, POST, PUT, DELETE, PATCH)
- Status codes (200, 201, 204, 400, 401, 404)
- Request/response body structure
- API versioning strategies

**Backend Development**
- FastAPI framework
- SQLAlchemy ORM
- Database modeling
- Authentication & authorization
- Input validation with Pydantic
- Error handling

**Frontend Development**
- HTML5 semantic markup
- CSS3 (Flexbox, Grid, Gradients)
- Vanilla JavaScript
- Async/await patterns
- API integration
- User experience design

**Security**
- Password hashing (bcrypt)
- JWT tokens
- CORS protection
- SQL injection prevention
- Input sanitization

**Full-Stack Development**
- Client-server communication
- Database persistence
- Environment configuration
- Error handling across layers
- Testing strategies

### Documentation Links

- **FastAPI**: https://fastapi.tiangolo.com/
- **Pydantic**: https://docs.pydantic.dev/
- **SQLAlchemy**: https://docs.sqlalchemy.org/
- **Python-Jose**: https://python-jose.readthedocs.io/
- **Azure**: https://docs.microsoft.com/azure/

---

## 🤝 Contributing

This is a learning project. To improve it:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Ideas for Enhancement

- [ ] Add priority levels to tasks
- [ ] Add task categories/tags
- [ ] Add task reminders/notifications
- [ ] Add team/shared tasks
- [ ] Add dark mode UI
- [ ] Add task search/filter
- [ ] Add task history/audit log
- [ ] Add mobile app (React Native)
- [ ] Add real-time updates (WebSockets)
- [ ] Add rate limiting

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🆘 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Use different port
uvicorn main:app --port 8002
```

**Module Not Found**
```bash
# Install dependencies again
pip install -r requirements.txt
```

**API Connection Error**
```bash
# Make sure server is running
# Check correct port in index.html
```

**Database Errors**
```bash
# Delete tasks.db and restart (recreates database)
rm tasks.db
```

See `TESTING.md` and `DEPLOYMENT.md` for more troubleshooting.

---

## 📞 Support

For issues or questions:

1. Check the documentation files
2. Review the code comments
3. Check the interactive API docs (`/docs`)
4. Review test file (`test_api.py`) for examples

---

## 🎓 Learning Path

1. **Week 1**: Understand REST API concepts
   - Read through code
   - Try manual API tests
   - Understand request/response flow

2. **Week 2**: Frontend-Backend Integration
   - Study JavaScript API calls
   - Test all frontend features
   - Debug in browser console

3. **Week 3**: Deployment
   - Set up Azure account
   - Deploy application
   - Monitor in production

4. **Week 4**: Enhancement
   - Add new features
   - Improve UI
   - Optimize performance

---

## ✅ Checklist: Ready for Production?

- [x] All endpoints tested
- [x] Frontend fully functional
- [x] Authentication working
- [x] Database persisting data
- [x] Error handling in place
- [x] Documentation complete
- [x] CORS configured
- [x] Ready for deployment
- [ ] Deployed to Azure
- [ ] Domain configured (optional)
- [ ] SSL enabled (Azure auto)
- [ ] Monitoring set up (optional)

---

## 🎉 Summary

**Student Task & Reminder API** is a complete, modern, production-ready web application that demonstrates professional software development practices. It's perfect for:

- Learning REST API design
- Understanding full-stack web development
- Practicing cloud deployment
- Building a portfolio project
- Teaching web development concepts

**Ready to deploy?** 🚀

See `DEPLOYMENT.md` for step-by-step Azure deployment instructions.

---

**Made with ❤️ for learning web development**

*Last Updated: January 25, 2026*
*Version: 1.0.0 - Production Ready*
