from sqlalchemy import select

from database import new_session, TaskORM
from schemas import SchemaTaskAdd, SchemaTaskList


class TaskRepository:
    @classmethod
    async def add_one(cls, data: SchemaTaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [SchemaTaskList.model_validate(task_model) for task_model in task_models]
            return task_schemas
