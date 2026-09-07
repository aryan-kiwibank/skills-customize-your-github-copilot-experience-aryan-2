# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that can return data, accept user input, and manage a simple collection of items.

## 📝 Tasks

### 🛠️	Create Your First API Route

#### Description
Create a FastAPI application with a home route that returns a welcome message as JSON.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Define a `GET /` route.
- Return a JSON response with a friendly welcome message.
- Run locally with Uvicorn.


### 🛠️	Return a List of Resources

#### Description
Add a route that returns a list of study resources from a Python list of dictionaries.

#### Requirements
Completed program should:

- Store at least three resources, each with an `id`, `title`, and `topic`.
- Define a `GET /resources` route.
- Return the full list of resources as JSON.
- Keep the response format consistent for every resource.


### 🛠️	Look Up One Resource

#### Description
Add a route that uses a path parameter to find one resource by its ID.

#### Requirements
Completed program should:

- Define a `GET /resources/{resource_id}` route.
- Return the matching resource when the ID exists.
- Return a helpful error message when the ID does not exist.
- Use FastAPI's `HTTPException` for missing resources.


### 🛠️	Add a New Resource

#### Description
Create a route that accepts new resource data from the request body and adds it to the collection.

#### Requirements
Completed program should:

- Define a Pydantic model for new resource data.
- Define a `POST /resources` route.
- Assign a new unique ID to each resource.
- Return the newly created resource as JSON.