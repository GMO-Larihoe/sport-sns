from pydantic import BaseModel


class PasswordReset(BaseModel):
    email: str
    password: str
