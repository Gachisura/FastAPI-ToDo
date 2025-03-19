import datetime
import fastapi
from lifespan import lifespan
import schema
import crud
import models
from dependencies import SessionDependency
from constants import STATUS_SUCCESS_RESPONSE


app = fastapi.FastAPI(
    title="ToDo",
    version="0.0.1",
    discription="A simple todo list API",
    lifespan=lifespan,
)


@app.get("/v1/todo/{todo_id}", response_model=schema.GetTodoResponse)
async def get_todo(todo_id: int, session: SessionDependency):
    todo = await crud.get_item(session, models.ToDo, todo_id)
    return todo.dict


@app.post("/v1/todo", response_model=schema.CreateTodoResponse)
async def create_todo(todo_json: schema.CreateTodoRequest, session: SessionDependency):
    todo = models.ToDo(**todo_json.dict())
    todo = await crud.add_item(session, todo)
    return todo.id_dict


@app.patch("/v1/todo/{todo_id}", response_model=schema.UpdateTodoResponse)
async def update_todo(todo_id: int, todo_json: schema.UpdateTodoRequest, session: SessionDependency):
    todo = await crud.get_item(session, models.ToDo, todo_id)
    todo_patch = todo_json.dict(exclude_unset=True)
    if todo_json.done:
        todo_patch['end_time'] = datetime.datetime.now()
    for field, value in todo_patch.items():
        setattr(todo, field, value)
    await crud.add_item(session, todo)
    return todo.id_dict


@app.delete("/v1/todo/{todo_id}", response_model=schema.DeleteTodoResponse, )
async def delite_todo(todo_id: int, session: SessionDependency):
    todo = await crud.get_item(session, models.ToDo, todo_id)
    await crud.delete_item(todo)
    return STATUS_SUCCESS_RESPONSE
