from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

resources = [
    {"id": 1, "title": "Python Functions Review", "topic": "functions"},
    {"id": 2, "title": "Dictionary Practice", "topic": "data structures"},
    {"id": 3, "title": "Intro to Web APIs", "topic": "apis"},
]


class NewResource(BaseModel):
    title: str
    topic: str


@app.get("/")
def read_home():
    return {"message": "Welcome to the study resources API!"}


@app.get("/resources")
def read_resources():
    return resources


@app.get("/resources/{resource_id}")
def read_resource(resource_id: int):
    for resource in resources:
        if resource["id"] == resource_id:
            return resource
    raise HTTPException(status_code=404, detail="Resource not found")


@app.post("/resources")
def create_resource(new_resource: NewResource):
    next_id = max(resource["id"] for resource in resources) + 1
    resource = {
        "id": next_id,
        "title": new_resource.title,
        "topic": new_resource.topic,
    }
    resources.append(resource)
    return resource