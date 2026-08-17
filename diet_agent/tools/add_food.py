from models import FoodEntry
from state import DietAgentState
from langchain.tools import tool

@tool
def add_food(state: DietAgentState, food: FoodEntry) -> DietAgentState:
    state.food_entries.append(food)
    return state