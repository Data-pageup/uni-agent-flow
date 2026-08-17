from pydantic import BaseModel 
from enum import Enum


class Goal(str, Enum):   # Goal -> the enum class,  (str,enum) -> base/parent classes
    """An enumeration representing different fitness goals."""
    LOSE_WEIGHT = "Lose weight"
    MAINTAIN_WEIGHT = "Maintain weight"
    GAIN_WEIGHT = "Gain weight"
    BUILD_MUSCLE = "Build muscle"
    GENERAL_FITNESS = "General fitness"


class WorkoutType(str,Enum):    
    """ An enumeration representing different workout types."""
    GYM = "Gym"
    HOME_WORKOUT = "Home workout"
    RUNNING = "Running"
    WALKING = "Walking"
    CYCLING = "Cycling"
    SWIMMING = "Swimming"
    SPORTS = "Sports"
    YOGA = "Yoga"
    OTHER = "Other"
    NONE = "No workout"
    
class DietType(str,Enum):
    """ An enumeration representing different diet types."""
    VEGETARIAN = "Vegetarian"
    NON_VEGETARIAN = "Non-vegetarian"
    VEGAN = "Vegan"
    EGGETARIAN = "Eggetarian"
    PESCATARIAN = "Pescatarian"
    OTHER = "Other"

class Focus(str, Enum):
    """An enumeration representing different training focus areas."""
    FULL_BODY = "Full body"
    UPPER_BODY = "Upper body"
    LOWER_BODY = "Lower body"
    CHEST = "Chest"
    BACK = "Back"
    SHOULDERS = "Shoulders"
    BICEPS = "Biceps"
    TRICEPS = "Triceps"
    LEGS = "Legs"
    CORE = "Core"
    GLUTES = "Glutes"
    CARDIO = "Cardio"
    ENDURANCE = "Endurance"
    FLEXIBILITY = "Flexibility"
    MOBILITY = "Mobility"
    OTHER = "Other"
  

class UserProfile(BaseModel):
    """A class representing a user's profile information."""
    name:str
    age:int
    sex:str
    height_cm:float
    weight_kg:float
    goal:Goal
    workout_type:WorkoutType
    diet_type:DietType
    
class FoodEntry(BaseModel):
    """A class representing a food entry with its food name, quantity and time ."""
    food_name:str
    quantity:float
    unit:str
    time:str


class WorkoutEntry(BaseModel):
    """A class representing a workout entry with its workout type, duration and time."""
    focus:Focus
    duration:int
    unit:str
    time:str 

class NutritionInfo(BaseModel):
    """A class representing the nutritional information of a food."""
    food_name: str
    calories: float
    protein_g: float
    carbs_g: float
    fat_g: float