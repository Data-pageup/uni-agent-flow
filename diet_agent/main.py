from models import UserProfile, Goal , WorkoutTypes

user = UserProfile(
    name="Ganesh",
    age="24",
    sex="Male",
    height_cm=178,
    weight_kg=74,
    goal= Goal.GENERAL_FITNESS,
    workout_type=WorkoutTypes.GYM,
    diet_type="Non-vegetarian"
)

print(user)

