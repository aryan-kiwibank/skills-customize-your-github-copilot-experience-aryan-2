# 📘 Assignment: SQLite-Powered API

## 🎯 Objective

Build a FastAPI application that saves and retrieves study resources from a SQLite database instead of storing data only in memory.

## 📝 Tasks

### 🛠️	Create the Database Table

#### Description
Set up a SQLite database table for storing study resources with a title and topic.

#### Requirements
Completed program should:

- Connect to a SQLite database named `resources.db`.
- Create a `resources` table if it does not already exist.
- Store each resource with an `id`, `title`, and `topic`.
- Run the database setup when the API starts.


### 🛠️	Read Resources from SQLite

#### Description
Update the API so the `GET /resources` route returns resources from the database.

#### Requirements
Completed program should:

- Query all rows from the `resources` table.
- Return the rows as a JSON list.
- Include each resource's `id`, `title`, and `topic` in the response.
- Return an empty list when no resources have been added yet.


### 🛠️	Add New Resources

#### Description
Create a route that accepts resource data from the request body and saves it to SQLite.

#### Requirements
Completed program should:

- Define a Pydantic model for incoming resource data.
- Define a `POST /resources` route.
- Insert each new resource into the database.
- Return the newly created resource, including its database ID.


### 🛠️	Find One Resource

#### Description
Create a route that looks up one resource by ID from the database.

#### Requirements
Completed program should:

- Define a `GET /resources/{resource_id}` route.
- Return the matching resource when it exists.
- Return a 404 error when the resource does not exist.
- Use FastAPI's `HTTPException` for the missing-resource response.