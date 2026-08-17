from pydantic import BaseModel 
from enum import Enum


class Goal(str, Enum):   # Goal -> the enum class,  (str,enum) -> base/parent classes
    """An enumeration representing different fitness goals."""
    LOSE_WEIGHT = "Lose weight"
    MAINTAIN_WEIGHT = "Maintain weight"
    GAIN_WEIGHT = "Gain weight"
    BUILD_MUSCLE = "Build muscle"
    GENERAL_FITNESS = "General fitness"


class WorkoutType(str,Enum):    # 
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
    


class UserProfile(BaseModel):
    """A class representing a user's profile information."""
    name:str
    age:int
    sex:str
    height_cm:float
    weight_kg:float
    goal:Goal
    workout_type:WorkoutTypes
    diet_type:str
    
