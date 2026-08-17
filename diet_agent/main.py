from models import (
    Focus,
    UserProfile,
    Goal,
    WorkoutType,
    DietType,
    FoodEntry,
    WorkoutEntry,
    NutritionInfo
)

from state import DietAgentState

from tools.add_food import add_food
from tools.add_workout import add_workout
from tools.nutrition import extract_nutrition
from tools.summary import daily_summary


user = UserProfile(
    name="Ganesh",
    age=24,
    sex="Male",
    height_cm=178,
    weight_kg=74,
    goal=Goal.GENERAL_FITNESS,
    workout_type=WorkoutType.GYM,
    diet_type="Non-vegetarian"
)

print(user)
print()


food = FoodEntry(
    food_name="Egg",
    quantity=2,
    unit="pieces",
    time="08:30 Am"
)

print(food)
print()


workout = WorkoutEntry(
    focus=Focus.CHEST,
    duration=45,
    unit="minutes",
    time="06:30 Am"
)

print(workout)
print()


state = DietAgentState(
    messages=[],
    user=user,
    food_entries=[],
    workout_entries=[],
    nutrition_entries=[],
    date="2026-08-17"
)

print(state)
print()


nutrition = extract_nutrition.invoke({
    "food": "2 eggs"
})

state.nutrition_entries.append(nutrition)

print(state.nutrition_entries)
print()


summary = daily_summary.invoke({
    "state": state
})

print(summary)