from datetime import datetime, timezone

import asyncio
import reflex as rx 

import sqlalchemy
from sqlmodel import Field


def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)

class ContactEntryModel(rx.Model, table=True):
    user_id: int | None = None
    first_name: str
    last_name: str | None = None
    email: str | None = None # = Field(nullable=True)
    message: str
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False
    )