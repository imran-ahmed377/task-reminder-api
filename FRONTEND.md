# Student Task & Reminder API - Web Frontend

A clean, modern, single-page web application for managing student tasks and reminders.

## Features

✨ **Authentication**
- User registration with email validation
- JWT-based login/logout
- Secure token storage (localStorage)

📋 **Task Management**
- Create tasks with title, description, and due date
- View all tasks
- Edit existing tasks
- Mark tasks as completed
- Delete tasks
- Visual indicators for completed tasks

🎨 **User Experience**
- Responsive design (works on desktop, tablet, mobile)
- Real-time task updates
- Clean, intuitive interface
- Alert notifications for actions
- No build tools required (vanilla HTML/CSS/JavaScript)

## How It Works

### Architecture

```
┌─────────────────────────────────────────┐
│   Web Browser (index.html)              │
│   - HTML/CSS/JavaScript                 │
│   - Task UI & Forms                     │
└──────────────┬──────────────────────────┘
               │ HTTP/JSON
               ↓
┌─────────────────────────────────────────┐
│   FastAPI Backend (main.py)             │
│   - /auth/register, /auth/login         │
│   - /tasks/* endpoints                  │
│   - JWT validation                      │
└──────────────┬──────────────────────────┘
               │ SQL Queries
               ↓
┌─────────────────────────────────────────┐
│   SQLite Database (tasks.db)            │
│   - Users table                         │
│   - Tasks table                         │
└─────────────────────────────────────────┘
```

## File Structure

```
RestAPI/
├── index.html              # Frontend (this file)
├── main.py                 # FastAPI app
├── requirements.txt        # Python dependencies
├── database.py             # DB configuration
├── models.py               # Pydantic schemas
├── routes.py               # Task endpoints
├── auth_routes.py          # Auth endpoints
├── auth.py                 # JWT utilities
├── db_models.py            # SQLAlchemy models
└── tasks.db                # SQLite database
```

## Running the Application

### 1. Start the API Server

```bash
# Activate virtual environment (if using one)
# Windows: rest_api_env\Scripts\activate
# Mac/Linux: source rest_api_env/bin/activate

# Start the server
uvicorn main:app --reload --host 127.0.0.1 --port 8001
```

The server will start at: `http://localhost:8001`

### 2. Open the Frontend

Once the server is running:
- Open your browser
- Navigate to: `http://localhost:8001`
- You'll see the Task Manager interface

## User Guide

### Registration

1. Fill in the **Register** form:
   - Username (unique)
   - Email
   - Password

2. Click **Register** button
3. Once successful, use those credentials to login

### Login

1. Fill in the **Login** form:
   - Username
   - Password

2. Click **Login** button
3. If successful, you'll see the task management interface

### Creating Tasks

1. Fill in the **Create New Task** form:
   - Task Title (required)
   - Description (optional)
   - Due Date (optional)

2. Click **Add Task** button
3. Task appears in the **Tasks** list below

### Managing Tasks

For each task, you can:

- **✓ Complete** - Mark task as complete (grays it out, adds strikethrough)
- **Edit** - Modify task details (button changes to "Update Task")
- **Delete** - Remove task permanently (asks for confirmation)

### Logging Out

Click the **Logout** button in the top right to logout and return to the auth form.

## Technical Details

### Frontend Technologies

- **HTML5** - Semantic markup
- **CSS3** - Gradient backgrounds, flexbox, grid, animations
- **JavaScript (ES6+)** - Async/await, fetch API, localStorage
- **Responsive Design** - Mobile-first approach with media queries

### Key JavaScript Functions

- `register()` - Handle user registration
- `login()` - Authenticate user
- `logout()` - Clear token and return to auth
- `loadTasks()` - Fetch and display tasks
- `createTask()` - Submit new task to API
- `updateTask(id)` - Update existing task
- `completeTask(id)` - Mark task as complete
- `deleteTask(id)` - Delete task with confirmation
- `apiCall(method, endpoint, body)` - Generic API request helper

### Error Handling

- All API errors are caught and displayed as alert messages
- Form validation prevents empty submissions
- Confirmation dialogs for destructive actions
- User-friendly error messages

### Security Notes

- JWT tokens stored in localStorage (accessible from dev tools)
- Production: Use httpOnly cookies for better security
- CORS enabled to allow frontend requests
- Password validation handled by API

## Customization

### Change API URL

Edit line 231 in `index.html`:

```javascript
const API_URL = 'http://localhost:8001';
```

Change `8001` to your API's port or URL.

### Customize Colors

Edit the CSS variables in `<style>` section:

```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);  /* Primary colors */
color: #667eea;  /* Accent color */
```

### Add More Fields

To add more task fields (e.g., priority, category):

1. Update the database model in `db_models.py`
2. Update Pydantic schema in `models.py`
3. Add form input in HTML
4. Update JavaScript task creation/editing

## Troubleshooting

### API Connection Error

**Problem**: "Unable to connect to the remote server"

**Solution**: 
1. Make sure the FastAPI server is running
2. Check the correct port (default: 8001)
3. Check `const API_URL` in index.html

### CORS Error

**Problem**: "Access to XMLHttpRequest blocked by CORS policy"

**Solution**: CORS is already enabled in `main.py` with `CORSMiddleware`

### Token Expired

**Problem**: "Invalid or expired token"

**Solution**:
1. Login again to get a new token
2. Token expires after 30 minutes

### Tasks Not Loading

**Problem**: Task list shows "Error loading tasks"

**Solution**:
1. Make sure you're logged in
2. Check browser console (F12) for errors
3. Verify API is running

## Browser Compatibility

- Chrome/Edge ✓
- Firefox ✓
- Safari ✓
- Mobile browsers ✓

## Next Steps

1. ✅ Frontend complete and running
2. ⭕ Test all features thoroughly
3. ⭕ Deploy to Azure App Service
4. ⭕ Point custom domain

## Support

For issues or questions:
- Check the console (F12 → Console tab) for JavaScript errors
- Check the Network tab to see API responses
- Verify credentials are correct
- Restart the FastAPI server

---

**Created with ❤️ for learning REST APIs and web development!**
