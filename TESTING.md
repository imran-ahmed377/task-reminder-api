# Student Task & Reminder API - Testing Guide

## Prerequisites
- Python 3.9+
- Dependencies installed: `pip install -r requirements.txt`
- Also install: `pip install requests` (for testing)

## Running the Server

### Option 1: Using main.py
```bash
python main.py
```
The API will be available at: `http://localhost:8000`

### Option 2: Using uvicorn directly
```bash
uvicorn main:app --reload
```

## Interactive API Documentation
Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Running Tests

### Automated Test Suite
Run all tests automatically:
```bash
python test_api.py
```

This will test:
1. ✓ Health check endpoint
2. ✓ User registration
3. ✓ Duplicate user rejection
4. ✓ User login
5. ✓ Invalid login handling
6. ✓ Create task (with auth)
7. ✓ Create task without auth (should fail)
8. ✓ Get all tasks
9. ✓ Get single task
10. ✓ Get non-existent task (404)
11. ✓ Update task
12. ✓ Mark task as completed
13. ✓ Delete task
14. ✓ Verify task deletion

### Manual Testing with cURL

#### 1. Health Check
```bash
curl -X GET http://localhost:8000/
```

#### 2. Register User
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password_123"
  }'
```

#### 3. Login User
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "secure_password_123"
  }'
```

**Note**: Copy the `access_token` from the response and use it in the Authorization header for protected endpoints.

#### 4. Create Task
```bash
curl -X POST http://localhost:8000/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Finish REST API project",
    "description": "Build backend using FastAPI",
    "due_date": "2026-02-01"
  }'
```

#### 5. Get All Tasks
```bash
curl -X GET http://localhost:8000/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

#### 6. Get Single Task (replace {id} with actual task ID)
```bash
curl -X GET http://localhost:8000/tasks/1 \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

#### 7. Update Task
```bash
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated title",
    "description": "Updated description"
  }'
```

#### 8. Mark Task as Completed
```bash
curl -X PATCH http://localhost:8000/tasks/1/complete \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

#### 9. Delete Task
```bash
curl -X DELETE http://localhost:8000/tasks/1 \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

### Testing with Postman

1. **Create a collection** named "Student Task API"

2. **Add requests**:
   - POST `/auth/register` - Register user
   - POST `/auth/login` - Get JWT token
   - POST `/tasks/` - Create task
   - GET `/tasks/` - List tasks
   - GET `/tasks/{id}` - Get task
   - PUT `/tasks/{id}` - Update task
   - PATCH `/tasks/{id}/complete` - Complete task
   - DELETE `/tasks/{id}` - Delete task

3. **Authentication**:
   - In the "Authorization" tab, select "Bearer Token"
   - Paste the token obtained from login response

## Expected Responses

### Success Responses
- **200 OK**: GET, PUT, PATCH successful
- **201 Created**: POST (create) successful
- **204 No Content**: DELETE successful

### Error Responses
- **400 Bad Request**: Invalid input or duplicate user
- **401 Unauthorized**: Invalid/missing JWT token
- **404 Not Found**: Task/user not found

## Database
The API uses SQLite. Database file: `tasks.db` (auto-created on first run)

## Troubleshooting

**Issue**: "Connection refused" error
- **Solution**: Make sure the server is running with `python main.py`

**Issue**: "Invalid token" error
- **Solution**: Make sure you're using a token obtained from `/auth/login`

**Issue**: "Dependency requires requests package"
- **Solution**: Install requests: `pip install requests`

## Next Steps
Once tests pass, proceed with Azure deployment!
