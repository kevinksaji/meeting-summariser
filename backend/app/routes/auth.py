# Router for handling authentication routes
# API Router allows us to define routes separately and then include them in main.py for better modularity

# import statements
from fastapi import APIRouter

# Create a new APIRouter instance
router = APIRouter()

# Define a route for testing authentication
@router.get("/test")
async def test_auth():
    return {"message": "Auth test successful!"}