from __future__ import annotations

from typing import List

from pydantic import BaseModel


class UsersList:
    class Datum(BaseModel):
        id: int
        email: str
        first_name: str
        last_name: str
        avatar: str

    class Support(BaseModel):
        url: str
        text: str

    class Model(BaseModel):
        page: int
        per_page: int
        total: int
        total_pages: int
        data: List[UsersList.Datum]
        support: UsersList.Support
