import datetime

from config import PG_DSN
from sqlalchemy import DateTime, Integer, String, func, Boolean
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    PG_DSN,
)

Session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass

    @property
    def id_dict(self):
        return {"id": self.id}


class ToDo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    important: Mapped[bool] = mapped_column(Boolean, default=False)
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    start_time: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    end_time: Mapped[datetime.datetime] = mapped_column(DateTime)

    @property
    def dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'important': self.important,
            'done': self.done,
            'start_time': self.start_time.isoformat()
        }


ORM_OBJECT = ToDo
ORM_CLS = type[ToDo]
