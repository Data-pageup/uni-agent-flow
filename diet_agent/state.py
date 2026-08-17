from models import UserProfile , FoodEntry , WorkoutEntry 



class DietAgentState:
    """A class representing the state of the diet agent."""
    user:UserProfile  
    food_entries:list[FoodEntry]
    workout_entries: list[WorkoutEntry]
    date:str
