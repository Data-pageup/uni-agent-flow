from models import Focus, UserProfile, Goal , WorkoutType , DietType , FoodEntry , WorkoutEntry

user = UserProfile(
    name="Ganesh",
    age="24",
    sex="Male",
    height_cm=178,
    weight_kg=74,
    goal= Goal.GENERAL_FITNESS,
    workout_type=WorkoutType.GYM,
    diet_type="Non-vegetarian"
)

print(user)

food = FoodEntry(
    food_name="Egg",
    quantity=2,
    unit="pieces",
    time="08:30 Am"
)

print(food)

Workout = WorkoutEntry(
    focus=Focus.CHEST,
    duration=45,
    unit="minutes",
    time="06:30 Am"
)

print(Workout)