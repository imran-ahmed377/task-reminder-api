# Azure Deployment Guide

## 📋 Pre-Deployment Checklist

- [x] Backend API complete and tested
- [x] Frontend built and integrated
- [x] Database schema finalized
- [x] Authentication working
- [x] All endpoints tested
- [x] Documentation written
- [ ] Azure account created
- [ ] Resource group set up
- [ ] App Service configured
- [ ] Database migrated (if using Azure SQL)
- [ ] Environment variables set
- [ ] Deployment completed

---

## 🔧 Deployment Steps (Overview)

### Step 1: Prepare Azure Account

1. Create free Azure account at https://azure.microsoft.com/free/
2. Create a resource group (e.g., "RestAPI-RG")
3. Set up budget alerts (optional but recommended)

### Step 2: Create App Service

**For both frontend and backend together:**

1. Create Azure App Service (Linux, Python 3.11)
2. Configure App Service Plan (B1 free tier works for learning)
3. Set runtime stack to Python 3.11

**Configuration:**
- Name: `student-task-api` (or your preferred name)
- Runtime: Python 3.11
- Region: Closest to your location
- Pricing: Free tier or B1 ($10/month)

### Step 3: Deploy Application

**Option A: Using Git (Recommended)**

```bash
# Initialize git repo
git init
git add .
git commit -m "Initial commit: Task API with frontend"

# Add Azure remote
az webapp up --name student-task-api --resource-group RestAPI-RG --runtime "python|3.11"

# Push to Azure
git push azure main
```

**Option B: Using ZIP deployment**

```bash
# Create deployment package
zip -r deploy.zip . -x "rest_api_env/*" "__pycache__/*" ".git/*"

# Upload to Azure (via portal or CLI)
az webapp deployment source config-zip -g RestAPI-RG -n student-task-api --src deploy.zip
```

### Step 4: Configure Environment

In Azure App Service, set environment variables:

```
DATABASE_URL=sqlite:///./tasks.db
SECRET_KEY=your-secure-random-key-here
CORS_ORIGINS=https://yourdomain.com
```

### Step 5: Set Startup Command

In Azure App Service Configuration:

```
gunicorn main:app --workers 4
```

Or for development:

```
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 📦 Required Files for Deployment

Make sure these files are in your project:

```
✓ index.html               - Frontend
✓ main.py                  - FastAPI app
✓ requirements.txt         - Dependencies
✓ all Python modules       - routes.py, auth.py, etc.
✓ .gitignore              - Exclude unnecessary files
✓ tasks.db                - Database (auto-created)
```

**Should NOT include:**
- `rest_api_env/` folder
- `__pycache__/` folders
- `.git/` folder
- `*.pyc` files

### .gitignore Content

```
# Virtual environment
rest_api_env/
venv/
env/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# IDEs
.vscode/
.idea/
*.swp

# Database
*.db

# Environment
.env
.env.local

# OS
.DS_Store
Thumbs.db
```

---

## 🔑 Important: Update Settings for Production

### 1. Change SECRET_KEY

In `.env` (Azure):

```env
SECRET_KEY=generate-a-random-secure-key-here
```

Generate using:
```python
import secrets
print(secrets.token_urlsafe(32))
```

### 2. Update CORS Settings

In `main.py`, change:

```python
# Current (allow all)
allow_origins=["*"]

# Production (specific domain)
allow_origins=["https://yourdomain.com"]
```

### 3. Use Azure SQL (Optional)

For production, replace SQLite with Azure SQL:

```python
# Update DATABASE_URL in .env
DATABASE_URL=mssql+pyodbc://user:password@server.database.windows.net/dbname?driver=ODBC+Driver+17+for+SQL+Server
```

### 4. Add Web Server

Install Gunicorn for production:

```bash
pip install gunicorn
```

Update requirements.txt:

```
gunicorn==21.2.0
```

---

## 🚀 Advanced: Using Docker (Optional)

For easier deployment, use Docker:

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
```

### requirements.txt (add these)

```
gunicorn==21.2.0
uvicorn[standard]==0.24.0
```

### Deploy Docker to Azure

```bash
# Create container registry
az acr create --resource-group RestAPI-RG --name mycontainerregistry --sku Basic

# Build and push
az acr build --registry mycontainerregistry --image student-task-api:latest .

# Create App Service from image
az appservice plan create --name RestAPI-Plan --resource-group RestAPI-RG --sku B1 --is-linux

az webapp create --resource-group RestAPI-RG --plan RestAPI-Plan --name student-task-api --deployment-container-image-name mycontainerregistry.azurecr.io/student-task-api:latest
```

---

## 🌐 Custom Domain Setup (Optional)

### Using Azure Custom Domain

1. In Azure Portal:
   - App Service → Custom Domains
   - Add a custom domain
   - Point your DNS records

2. Update CORS in code:

```python
allow_origins=["https://yourdomain.com"]
```

### Using a Free Domain

Services like:
- Freenom.com (free .tk, .ml domains)
- DuckDNS (free dynamic DNS)
- GitHub Pages (for frontend only)

---

## 🔍 Testing After Deployment

### Health Check

```bash
curl https://student-task-api.azurewebsites.net/api/health
```

Expected response:
```json
{"message": "Student Task & Reminder API is running!"}
```

### Test Frontend

```
https://student-task-api.azurewebsites.net
```

Should see the Task Manager interface.

### Test API

```bash
curl https://student-task-api.azurewebsites.net/docs
```

Should see Swagger UI documentation.

---

## 📊 Monitoring & Logs

### View Logs

In Azure Portal:
- App Service → Log Stream
- Or via CLI: `az webapp log tail -g RestAPI-RG -n student-task-api`

### Set Up Alerts

- CPU usage > 80%
- Memory usage > 80%
- HTTP 5xx errors
- Response time > 2 seconds

### Application Insights (Optional)

Enable for performance monitoring:

```bash
az monitor app-insights create --resource-group RestAPI-RG --location eastus --app student-task-api
```

---

## 💾 Database Migration to Azure SQL

### Create Azure SQL Database

```bash
az sql server create --name student-task-sql --resource-group RestAPI-RG --location eastus --admin-user sqladmin --admin-password YourPassword123!

az sql db create --server student-task-sql --resource-group RestAPI-RG --name taskdb
```

### Connect from App

Update `.env`:

```
DATABASE_URL=mssql+pyodbc://sqladmin:YourPassword123!@student-task-sql.database.windows.net/taskdb?driver=ODBC+Driver+17+for+SQL+Server
```

### Install ODBC Driver

```bash
pip install pyodbc
```

---

## ⚠️ Troubleshooting Deployment

### Application Not Starting

Check logs:
```bash
az webapp log tail -g RestAPI-RG -n student-task-api
```

Common issues:
- Missing `requirements.txt`
- Wrong Python version
- Module import errors
- Database file not writable

### 502 Bad Gateway

Usually means app crashed. Check:
- Startup command correct
- All dependencies installed
- No import errors in main.py

### Static Files Not Loading

Make sure:
- `index.html` is in root directory
- `main.py` has `FileResponse("index.html")` on `/`
- No custom static file directory needed

### Database Permission Error

If using SQLite:
- Change to app-generated database path
- Or use Azure SQL instead

---

## 📝 Cost Estimation (Azure)

| Service | Free Tier | Minimum Cost |
|---------|-----------|--------------|
| App Service | 1 B1 free | $10/month |
| SQL Database | No free | $5-50/month |
| Storage | 5GB free | $0.024/GB |
| Traffic | 1GB outbound | $0.12/GB |

**Recommendation**: Start with free App Service + SQLite (no additional costs beyond server)

---

## 🎯 Next Steps After Deployment

1. ✅ Test all features on production
2. ✅ Monitor performance
3. ✅ Set up custom domain (optional)
4. ✅ Enable HTTPS/SSL (automatic with Azure)
5. ✅ Set up backup strategy
6. ✅ Monitor costs
7. ✅ Plan for scaling

---

## 🆘 Need Help?

- Azure Docs: https://docs.microsoft.com/azure/
- FastAPI Docs: https://fastapi.tiangolo.com/
- SQLAlchemy Docs: https://docs.sqlalchemy.org/

---

**Ready to deploy! 🚀**
