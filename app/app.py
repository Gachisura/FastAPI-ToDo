import fastapi
import pydantic
from lifespan import lifespan


app = fastapi.FastAPI(
    title="ToDo",
    version="0.0.1",
    discription="A simple todo list API",
    lifespan=lifespan,
)
