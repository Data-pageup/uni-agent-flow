from models import Focus, UserProfile, Goal , WorkoutType , DietType , FoodEntry , WorkoutEntry
from state import DietAgentState 
from tools.add_food import add_food

user = UserProfile(
    name="Ganesh",
    age=24,
    sex="Male",
    height_cm=178,
    weight_kg=74,
    goal= Goal.GENERAL_FITNESS,
    workout_type=WorkoutType.GYM,
    diet_type="Non-vegetarian"
)

print(user)

print( )
food = FoodEntry(
    food_name="Egg",
    quantity=2,
    unit="pieces",
    time="08:30 Am"
)

print(food)
print( )

Workout = WorkoutEntry(
    focus=Focus.CHEST,
    duration=45,
    unit="minutes",
    time="06:30 Am"
)

print(Workout)
print( )


state = DietAgentState(
    user =user,
    food_entries = [food],
    workout_entries=[Workout],
    date = "2026-08-17"
)
print(state)


print(add_food)