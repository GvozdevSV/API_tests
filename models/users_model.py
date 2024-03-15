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


class RequestUser:
    class Model(BaseModel):
        name: str = "morpheus"
        job: str = 'leader'


class ResponseCreateUser:
    class Model(BaseModel):
        name: str
        job: str
        id: str
        createdAt: str


class ResponsePutUser:
    class Model(BaseModel):
        name: str
        job: str
        updatedAt: str


class SingleUser:
    class Data(BaseModel):
        id: int
        email: str
        first_name: str
        last_name: str
        avatar: str

    class Support(BaseModel):
        url: str
        text: str

    class Model(BaseModel):
        data: SingleUser.Data
        support: SingleUser.Support
