from state import DietAgentState
from langchain.tools import tool


@tool
def daily_summary(state: DietAgentState) -> str:
    """Provide a summary of the user's food and workout entries for today."""

    summary = f"Date: {state.date}\n\n"

    summary += "Food consumed:\n"

    for food in state.food_entries:
        summary += (
            f"- {food.food_name}: "
            f"{food.quantity} {food.unit} at {food.time}\n"
        )

    summary += "\nWorkouts:\n"

    for workout in state.workout_entries:
        summary += (
            f"- {workout.focus.value}: "
            f"{workout.duration} {workout.unit} at {workout.time}\n"
        )

    return summary