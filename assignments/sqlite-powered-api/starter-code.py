import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DATABASE_NAME = "resources.db"

app = FastAPI()


class NewResource(BaseModel):
    title: str
    topic: str


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def setup_database():
    connection = get_connection()
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            topic TEXT NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()


@app.on_event("startup")
def startup():
    setup_database()


@app.get("/")
def read_home():
    return {"message": "Welcome to the SQLite-powered resources API!"}


@app.get("/resources")
def read_resources():
    connection = get_connection()
    rows = connection.execute("SELECT id, title, topic FROM resources").fetchall()
    connection.close()
    return [dict(row) for row in rows]


@app.post("/resources")
def create_resource(new_resource: NewResource):
    connection = get_connection()
    cursor = connection.execute(
        "INSERT INTO resources (title, topic) VALUES (?, ?)",
        (new_resource.title, new_resource.topic),
    )
    connection.commit()
    resource_id = cursor.lastrowid
    connection.close()
    return {"id": resource_id, "title": new_resource.title, "topic": new_resource.topic}


@app.get("/resources/{resource_id}")
def read_resource(resource_id: int):
    connection = get_connection()
    row = connection.execute(
        "SELECT id, title, topic FROM resources WHERE id = ?",
        (resource_id,),
    ).fetchone()
    connection.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Resource not found")

    return dict(row)