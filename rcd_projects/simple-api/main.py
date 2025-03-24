from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import random

app = FastAPI()

# Sample data representing side hustles
side_hustles = [
  {
    "id": 1,
    "name": "Freelance Writing",
    "category": "Writing",
    "estimated_earnings": "$500 - $3000/month",
    "skills_required": ["Writing", "SEO", "Research"],
    "difficulty": "Medium"
  },
  {
    "id": 2,
    "name": "Dropshipping",
    "category": "E-Commerce",
    "estimated_earnings": "$1000 - $10,000/month",
    "skills_required": ["Marketing", "Product Research", "Customer Service"],
    "difficulty": "Hard"
  },
  {
    "id": 3,
    "name": "Affiliate Marketing",
    "category": "Marketing",
    "estimated_earnings": "$100 - $5000/month",
    "skills_required": ["Content Creation", "SEO", "Social Media"],
    "difficulty": "Medium"
  },
  {
    "id": 4,
    "name": "Graphic Design",
    "category": "Design",
    "estimated_earnings": "$500 - $5000/month",
    "skills_required": ["Adobe Photoshop", "Illustrator", "Creativity"],
    "difficulty": "Medium"
  },
  {
    "id": 5,
    "name": "YouTube Channel",
    "category": "Content Creation",
    "estimated_earnings": "$100 - $10,000+/month",
    "skills_required": ["Video Editing", "Storytelling", "Marketing"],
    "difficulty": "Hard"
  }
]

# Pydantic model for request validation
class SideHustle(BaseModel):
    id: int
    name: str
    category: str
    estimated_earnings: str
    skills_required: list[str]
    difficulty: str

# Root endpoint returning all side hustles
@app.get("/")
def hustles():
    return side_hustles

# Endpoint to get a random side hustle
@app.get("/side_hustles")
def get_side_hustles():
    return {"side_hustle": random.choice(side_hustles)}

# Endpoint to create a new side hustle
@app.post("/hustles")
def create_hustle(hustle: SideHustle):
    new_id = max([h["id"] for h in side_hustles], default=0) + 1  # Auto-generate ID
    new_hustle = hustle.dict()
    new_hustle["id"] = new_id  # Assign new ID
    side_hustles.append(new_hustle)  # Append new hustle
    return {"message": "Side hustle added successfully!", "hustle": new_hustle}

# Endpoint to update an existing side hustle by ID
@app.put("/hustles/{id}")
def update_hustle(id: int, updated_hustle: SideHustle):
    for hustle in side_hustles:
        if hustle["id"] == id:
            # Update the existing hustle data
            hustle["name"] = updated_hustle.name
            hustle["category"] = updated_hustle.category
            hustle["estimated_earnings"] = updated_hustle.estimated_earnings
            hustle["skills_required"] = updated_hustle.skills_required
            hustle["difficulty"] = updated_hustle.difficulty
            return {"message": "Side hustle updated successfully!", "hustle": hustle}
    
    # Raise error if hustle not found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Side hustle with ID {id} not found"
    )

# Endpoint to delete a side hustle by ID
@app.delete("/hustles/{id}")
def delete_hustle(id: int):
    for index, hustle in enumerate(side_hustles):
        if hustle["id"] == id:
            deleted_hustle = side_hustles.pop(index)  # Remove hustle from list
            return {"Message": "Side hustle deleted successfully!", "deleted_hustle": deleted_hustle}
    
    # Raise error if hustle not found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Side hustle with ID {id} not found"
    )