# Quick Start Guide

## Prerequisites

- Python 3.11+ installed
- Virtual environment created (optional but recommended)

## Setup Steps

### 1. Install Dependencies

```bash
cd "c:\Users\Asus\Desktop\Skills Upgrade\RestAPI"
pip install -r requirements.txt
```

### 2. Start the API Server

```bash
# Option A: Using uvicorn directly (Recommended)
uvicorn main:app --host 127.0.0.1 --port 8001 --reload

# Option B: Using Python directly  
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8001 (Press CTRL+C to quit)
```

### 3. Open the Web Interface

Open your browser and go to:
```
http://localhost:8001
```

You'll see the Task Manager interface!

## Usage

1. **Register** - Create a new account
2. **Login** - Log in with your credentials
3. **Create Tasks** - Add tasks with optional description and due date
4. **Manage Tasks** - Complete, edit, or delete tasks
5. **Logout** - Exit when done

## Project Structure

```
RestAPI/
├── index.html              # 🎨 Web Frontend (YOUR BROWSER DISPLAYS THIS)
├── main.py                 # 🔧 FastAPI Application
├── requirements.txt        # 📦 Python Dependencies
├── routes.py               # 📋 Task API Endpoints
├── auth_routes.py          # 🔐 Authentication Endpoints
├── database.py             # 💾 Database Configuration
├── db_models.py            # 📊 Database Models
├── auth.py                 # 🔑 JWT & Password Utilities
├── models.py               # 📝 API Request/Response Schemas
├── test_api.py             # 🧪 Automated Tests
├── TESTING.md              # 📖 Testing Guide
├── FRONTEND.md             # 🎨 Frontend Documentation
└── tasks.db                # 💾 SQLite Database (Auto-created)
```

## API Documentation

Once server is running, visit:

- **Swagger UI** (Interactive): http://localhost:8001/docs
- **ReDoc** (Read-only): http://localhost:8001/redoc

## Environment Variables

Edit `.env` file to customize:

```env
DATABASE_URL=sqlite:///./tasks.db
SECRET_KEY=your-super-secret-key-change-in-production-12345
```

## Troubleshooting

### Port Already in Use

If port 8001 is already in use:

```bash
uvicorn main:app --host 127.0.0.1 --port 8002 --reload
```

Then access at `http://localhost:8002`

### Module Not Found Errors

Make sure you activated virtual environment:

```bash
# Windows
rest_api_env\Scripts\activate

# Mac/Linux  
source rest_api_env/bin/activate
```

### CORS or Connection Issues

1. Make sure server is running (check console output)
2. Check the correct port in browser
3. Wait 2-3 seconds after starting server before opening browser

## What You Can Learn

✅ REST API Design  
✅ FastAPI Framework  
✅ JWT Authentication  
✅ SQLAlchemy ORM  
✅ Frontend-Backend Integration  
✅ Vanilla JavaScript (No frameworks!)  
✅ Responsive Web Design  
✅ HTTP Methods & Status Codes  
✅ Database Modeling  
✅ Cloud Deployment (Next!)  

## Next: Azure Deployment

Once you're happy with the application:

1. Create Azure Account (free tier available)
2. Deploy API to Azure App Service
3. Deploy Frontend alongside API
4. Set up custom domain (optional)

See `DEPLOYMENT.md` for detailed steps.

---

**Happy learning! 🚀**
