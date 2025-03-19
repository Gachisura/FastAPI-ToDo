import datetime
from typing import Literal

from pydantic import BaseModel


class IdReturnBase(BaseModel):
    id: int


class StatusSuccessBase(BaseModel):
    status: Literal["success"]


class GetTodoResponse(BaseModel):

    id: int
    title: str
    description: str
    important: bool
    done: bool
    start_time: datetime.datetime
    end_time: datetime.datetime | None = None


class CreateTodoRequest(BaseModel):
    title: str
    description: str
    important: bool = False
    done: bool = False


class CreateTodoResponse(IdReturnBase):
    pass


class UpdateTodoRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    important: bool | None = None
    done: bool | None = None


class UpdateTodoResponse(IdReturnBase):
    pass


class DeleteTodoResponse(StatusSuccessBase):
    pass
