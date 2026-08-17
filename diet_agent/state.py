from typing import Annotated
from pydantic import BaseModel
from langgraph.graph.message import add_messages

from models import UserProfile, FoodEntry, WorkoutEntry, NutritionInfo


class DietAgentState(BaseModel):
    messages: Annotated[list, add_messages]

    user: UserProfile
    food_entries: list[FoodEntry]
    workout_entries: list[WorkoutEntry]
    nutrition_entries: list[NutritionInfo]
    date: str