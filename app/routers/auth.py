from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.config import EnvConfig
from app.models.entities import (
    AdminDataModel,
    AdminResponseModel,
    PurchasesModel,
    ReportsModel,
    TokenModel,
    UserDataModel,
    UserModel,
    UserResponseModel,
)
from app.services.auth import authenticate_user, create_access_token, get_current_user
from app.services.db import fake_purchases_db, fake_reports_db, fake_users_db

ACCESS_TOKEN_EXPIRE_MINUTES = EnvConfig.access_token_expire_minutes

router = APIRouter()


@router.post("/token")
async def login_for_access_token(
    username: str = Query(...), password: str = Query(...)
) -> TokenModel:
    user = authenticate_user(fake_users_db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return TokenModel(access_token=access_token, token_type="bearer")


@router.get("/user", response_model=UserResponseModel)
async def read_user(
    current_user: Annotated[UserModel, Depends(get_current_user)],
):
    if current_user.role != "user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return UserResponseModel(
        message=f"Hello, {current_user.username}!",
        data=UserDataModel(
            name=current_user.name,
            email=current_user.email,
            purchases=[
                PurchasesModel(**purchase)
                for purchase in fake_purchases_db.get(current_user.username, [])
            ],
        ),
    )


@router.get("/admin", response_model=AdminResponseModel)
async def read_admin(
    current_user: Annotated[UserModel, Depends(get_current_user)],
):
    if current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return AdminResponseModel(
        message=f"Hello, {current_user.username}!",
        data=AdminDataModel(
            name=current_user.name,
            email=current_user.email,
            reports=[
                ReportsModel(**report) for report in fake_reports_db.get(current_user.username, [])
            ],
        ),
    )
