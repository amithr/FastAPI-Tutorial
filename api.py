from typing import Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


# https://www.toptal.com/python/build-high-performing-apps-with-the-python-fastapi-framework


# We could call this whatever we want
app = FastAPI()

origins = ["*"]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Employee(BaseModel):
    name: str
    id: Optional[int]
    position: Optional[str] = None


# JSON Store
app.state.employees = [
    {"name": "Amith", "id":1, "position": "Software Engineer"},
    {"name": "Aiden", "id":2, "position": "Teacher"},
    {"name":"Olya", "id":3, "position":"Professor"}
]


@app.get("/")
async def hello_world():
    return {"message": "hello world"}

@app.get("/employees")
async def employees():
    return app.state.employees

# Making a PUT request repeatedly does not cause a new action
# Request parameters
@app.put("/create/employee")
async def create_employee(employee:Employee):
    employee.id = len(app.state.employees)+1
    app.state.employees.append(employee.dict())
    return app.state.employees

# Making the same POST request repeatedly causes the same action multiple times
# Request parameters
@app.post("/update/employee")
async def update_employee(request:Request):
    data = await request.json()
    employee_id = int(data['employee_id'])
    key = data['key']
    value = data['value']
    for employee in app.state.employees:
        if employee['id'] == employee_id:
            employee[key] = value
    return app.state.employees

@app.delete("/delete/employee/{employee_id}")
async def delete_employee(employee_id:int):
    print(employee_id)
    for employee in app.state.employees:
        if employee['id'] == employee_id:
            app.state.employees.remove(employee)
            return app.state.employees
    return None