from models import UserProfile , FoodEntry , WorkoutEntry 
from pydantic import BaseModel
from models import NutritionInfo



class DietAgentState(BaseModel):
    """A class representing the state of the diet agent."""
    user:UserProfile  
    food_entries:list[FoodEntry]
    workout_entries: list[WorkoutEntry]
    nutrition_entries: list[NutritionInfo]
    date:str
