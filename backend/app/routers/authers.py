from fastapi import Response, status, APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_

from datetime import datetime, timedelta, timezone
from typing import List, Any

router = APIRouter(
    prefix="/api/authers",
    tags=["authers"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
def get_data():
    users: list[dict[str, Any]] = []
    user: dict[str, Any] = dict()
    user['id'] = 1
    user['name'] = 'sample'
    users.append(user)
    user: dict[str, Any] = dict()
    user['id'] = 2
    user['name'] = 'test'
    users.append(user)
    user: dict[str, Any] = dict()
    user['id'] = 3
    user['name'] = 'taro'
    users.append(user)
    return users