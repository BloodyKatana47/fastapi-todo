from typing import Optional

from pydantic import BaseModel


class SchemaTaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class SchemaTaskList(SchemaTaskAdd):
    id: int


class SchemaTaskID(BaseModel):
    ok: bool = True
    task_id: int
