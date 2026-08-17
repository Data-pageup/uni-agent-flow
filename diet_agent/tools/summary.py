from state import DietAgentState
from langchain.tools import tool


@tool
def daily_summary(state: DietAgentState) -> str:
    """Provide a summary of the user's food, nutrition and workout entries for today."""

    summary = f"Date: {state.date}\n\n"

    summary += "Food consumed:\n"

    for food in state.food_entries:
        summary += (
            f"- {food.food_name}: "
            f"{food.quantity} {food.unit} at {food.time}\n"
        )

    summary += "\nNutrition:\n"

    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for nutrition in state.nutrition_entries:
        total_calories += nutrition.calories
        total_protein += nutrition.protein_g
        total_carbs += nutrition.carbs_g
        total_fat += nutrition.fat_g

    summary += f"- Calories: {total_calories:.2f} kcal\n"
    summary += f"- Protein: {total_protein:.2f} g\n"
    summary += f"- Carbs: {total_carbs:.2f} g\n"
    summary += f"- Fat: {total_fat:.2f} g\n"

    summary += "\nWorkouts:\n"

    for workout in state.workout_entries:
        summary += (
            f"- {workout.focus.value}: "
            f"{workout.duration} {workout.unit} at {workout.time}\n"
        )

    return summary