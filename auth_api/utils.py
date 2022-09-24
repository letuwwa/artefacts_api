import os
import jwt
from datetime import datetime, timedelta


def create_access_token(user_id: str) -> str:
    return jwt.encode(
        payload={
            "id": user_id,
            "iat": datetime.now(),
            "exp": datetime.now() + timedelta(seconds=30),
        },
        algorithm="HS256",
        key=os.environ.get("jwt_secret_access_key"),
    )


def create_refresh_token(user_id: str) -> str:
    return jwt.encode(
        payload={
            "id": user_id,
            "iat": datetime.now(),
            "exp": datetime.now() + timedelta(hours=1),
        },
        algorithm="HS256",
        key=os.environ.get("jwt_secret_refresh_key"),
    )
