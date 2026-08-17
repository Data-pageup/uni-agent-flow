from models import FoodEntry
from state import DietAgentState


def add_food(state:DietAgentState, food:FoodEntry) -> DietAgentState:
    state.food_entries.append(food)
    return state 

