from fastapi import FastAPI, WebSocket, Depends, status
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from database import engine, Base, get_db
from db_models import Task
from auth_db_models import User
from routes import router as task_router
from auth_routes import router as auth_router, get_current_user
from websocket_manager import manager
from auth import verify_access_token

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Task & Reminder API", version="1.0.0")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(task_router)
app.include_router(auth_router)


@app.get("/")
def read_root():
    """Serve the frontend HTML"""
    return FileResponse("index.html")


@app.get("/api/health")
def health_check():
    """Health check endpoint"""
    return JSONResponse(
        {"message": "Student Task & Reminder API is running!"},
        status_code=200
    )


@app.websocket("/ws/{token}")
async def websocket_endpoint(websocket: WebSocket, token: str):
    """WebSocket endpoint for real-time task updates"""
    try:
        # Verify the token and get user_id
        user_id = verify_access_token(token)
        if not user_id:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            return

        user_id = int(user_id)
        await manager.connect(websocket, user_id)

        try:
            while True:
                # Keep connection alive, client sends pings
                data = await websocket.receive_text()
        except Exception:
            pass
    finally:
        if user_id:
            await manager.disconnect(user_id, websocket)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
