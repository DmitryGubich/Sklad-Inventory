import uuid
from enum import Enum

from sqlmodel import Field, SQLModel


class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"


class User(SQLModel, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)
    public_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    role: UserRole = Field(default=UserRole.USER, max_length=254)
