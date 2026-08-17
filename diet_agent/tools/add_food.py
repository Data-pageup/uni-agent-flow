from models import FoodEntry
from langchain.tools import tool, ToolRuntime
from state import DietAgentState


@tool
def add_food(
    food: FoodEntry,
    runtime: ToolRuntime[DietAgentState]
) -> str:
    """Add a food entry to the user's daily food log."""

    runtime.state["food_entries"].append(food)

    return f"Added {food.food_name} to today's food log."