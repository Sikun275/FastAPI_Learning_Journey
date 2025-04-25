from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

tasks_db = []

# this is the Pydantic model for data validation
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    done: bool = False

# POST, GET, PUT, DELETE (create, read, update, delete)

# add a new task
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task.dict())
    return task

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Validate user credentials
    # Return JWT token

# root point 
@app.get("/")
def home():
    return {"message": "Welcome to the my FastAPI learning homepage!"}

# get all tasks
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db

@app.get("/tasks/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )
    return task

# get a task by id
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# update a task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for i, t in enumerate(tasks_db):
        if t["id"] == task_id:
            tasks_db[i] = updated_task.dict()
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    for i, t in enumerate(tasks_db):
        if t["id"] == task_id:
            tasks_db.pop(i)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")