from models import FoodEntry
from state import DietAgentState
from langchain.tools import tool


@tool
def add_food(state: DietAgentState, food: FoodEntry) -> DietAgentState:
    """Add a food entry to the user's daily food log."""

    state.food_entries.append(food)
    return state