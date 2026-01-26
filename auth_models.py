from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    """Base user model"""
    username: str
    email: Optional[str] = None


class UserCreate(UserBase):
    """Model for user registration"""
    password: str


class UserLogin(BaseModel):
    """Model for user login"""
    username: str
    password: str


class UserResponse(UserBase):
    """Model for user response"""
    id: int

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """Model for authentication token response"""
    access_token: str
    token_type: str = "bearer"
