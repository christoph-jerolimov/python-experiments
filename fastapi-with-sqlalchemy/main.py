from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from fastapi_cli.cli import main
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from db import init_db, get_session, NewTodo, UpdateTodo, TodoResponse, Todo
from typing import Optional, AsyncIterator


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/todos", response_model=TodoResponse)
def create_todo(newTodo: NewTodo, session: Session = Depends(get_session)) -> Todo:
    todo = Todo()
    todo.name = newTodo.name
    if isinstance(newTodo.done, bool):
        todo.done = newTodo.done
    session.add(todo)
    session.commit()
    return todo


@app.get("/todos", response_model=list[TodoResponse])
def get_todos(session: Session = Depends(get_session)) -> list[Todo]:
    return session.query(Todo).all()


@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo_by_todo_id(
    todo_id: int, session: Session = Depends(get_session)
) -> Todo | JSONResponse:
    todo: Todo | None = session.query(Todo).get(todo_id)
    if not todo:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "Todo not found"}
        )
    return todo


@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo_by_todo_id(
    todo_id: int, updateTodo: UpdateTodo, session: Session = Depends(get_session)
) -> Todo | JSONResponse:
    todo: Optional[Todo] = session.query(Todo).get(todo_id)
    if not todo:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "Todo not found"}
        )
    if name := updateTodo.name:
        todo.name = name
    if done := updateTodo.done:
        todo.done = done
    session.commit()
    return todo


@app.delete("/todos/{todo_id}")
def delete_todo_by_todo_id(
    todo_id: int, session: Session = Depends(get_session)
) -> JSONResponse:
    # or how can we run a delete query directly?
    todo: Todo | None = session.query(Todo).get(todo_id)
    if not todo:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "Todo not found"}
        )
    session.delete(todo)
    session.commit()
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED, content={"message": "Todo deleted"}
    )


if __name__ == "__main__":
    main()
