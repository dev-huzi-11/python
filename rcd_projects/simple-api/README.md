# Side Hustle API

This is a simple FastAPI-based REST API for managing side hustles. The API allows to retrieve, add, update, and delete different side hustles with relevant details.

## Features
- Retrieve a list of side hustles
- Get a random side hustle
- Add a new side hustle
- Update an existing side hustle
- Delete a side hustle by ID

## Installation & Setup
1. Create a new project folder and navigate into it:
   ```sh
   mkdir simple-api && cd simple-api
   ```

2. Initialize the project using `uv`:
   ```sh
   uv init simple-api
   cd simple-api
   ```

3. Install FastAPI:
   ```sh
   uv add fastapi[standard]
   ```

4. Activate the virtual environment (for Git Bash):
   ```sh
   source .venv/Scripts/activate
   ```

## Running the API
Start the FastAPI server using Uvicorn:
```sh
fastapi dev main.py
```

## API Endpoints

### Get All Side Hustles
**Endpoint:** `GET /`

**Response:**
```json
[
    {
        "id": 1,
        "name": "Freelance Writing",
        "category": "Writing",
        "estimated_earnings": "$500 - $3000/month",
        "skills_required": ["Writing", "SEO", "Research"],
        "difficulty": "Medium"
    }
]
```

### Get a Random Side Hustle
**Endpoint:** `GET /side_hustles`

**Response:**
```json
{
    "side_hustle": { "id": 3, "name": "Affiliate Marketing", ... }
}
```

### Create a Side Hustle
**Endpoint:** `POST /hustles`

**Request Body:**
```json
{
    "id": 6,
    "name": "Web Development",
    "category": "Tech",
    "estimated_earnings": "$1000 - $5000/month",
    "skills_required": ["HTML", "CSS", "JavaScript"],
    "difficulty": "Medium"
}
```

**Response:**
```json
{
    "message": "Side hustle added successfully!",
    "hustle": { "id": 6, "name": "Web Development", ... }
}
```

### Update a Side Hustle
**Endpoint:** `PUT /hustles/{id}`

**Request Body:** Similar to `POST /hustles`

**Response:**
```json
{
    "message": "Side hustle updated successfully!",
    "hustle": { "id": 6, "name": "Updated Name", ... }
}
```

### Delete a Side Hustle
**Endpoint:** `DELETE /hustles/{id}`

**Response:**
```json
{
    "Message": "Side hustle deleted successfully!",
    "deleted_hustle": { "id": 6, "name": "Web Development", ... }
}
```