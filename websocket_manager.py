from fastapi import WebSocket
from typing import List, Dict, Set
import json


class WebSocketManager:
    """Manages WebSocket connections for real-time updates"""

    def __init__(self):
        # Store active connections: {user_id: [websocket, ...]}
        self.active_connections: Dict[int, Set[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, user_id: int):
        """Add a new WebSocket connection"""
        await websocket.accept()
        if user_id not in self.active_connections:
            self.active_connections[user_id] = set()
        self.active_connections[user_id].add(websocket)

    async def disconnect(self, user_id: int, websocket: WebSocket):
        """Remove a WebSocket connection"""
        if user_id in self.active_connections:
            self.active_connections[user_id].discard(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]

    async def broadcast_to_user(self, user_id: int, message: dict):
        """Send a message to all connections of a specific user"""
        if user_id in self.active_connections:
            disconnected = []
            for connection in self.active_connections[user_id]:
                try:
                    await connection.send_json(message)
                except Exception:
                    disconnected.append(connection)

            # Remove disconnected connections
            for connection in disconnected:
                await self.disconnect(user_id, connection)

    async def broadcast_to_all(self, message: dict):
        """Send a message to all connected clients"""
        for user_id in list(self.active_connections.keys()):
            await self.broadcast_to_user(user_id, message)


# Global instance
manager = WebSocketManager()
