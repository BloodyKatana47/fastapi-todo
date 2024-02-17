from typing import Optional

from pydantic import BaseModel, ConfigDict


class SchemaTaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class SchemaTaskList(SchemaTaskAdd):
    id: int


class SchemaTaskID(BaseModel):
    ok: bool = True
    task_id: int
