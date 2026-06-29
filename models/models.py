from pydantic import BaseModel, EmailStr, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    name: str
    email: EmailStr
    is_active: bool


class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True


class UpdateUserRequest(BaseModel):
    name: str
    email: EmailStr
    is_active: bool