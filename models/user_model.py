# Модели (Pydantic) — для валидации данных.
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class RegisterRequest(BaseModel):
    first_name: str = Field(..., title="Ваше имя", max_length=30, min_length=1)
    email: EmailStr = Field(..., title="Email", max_length=254, min_length=1)
    password: str = Field(..., title="Пароль", max_length=128, min_length=6)

    is_tutor: Optional[bool] = Field(True, title="Я репетитор")
    is_premium: Optional[bool] = Field(False, title="Is premium")
    is_standart: Optional[bool] = Field(False, title="Is standart")
    is_writer: Optional[bool] = Field(False, title="Is writer")
    end_subscription: Optional[str] = Field(
        None, title="End subscription", json_schema_extra={"nullable": True}
    )
