from langchain_groq import ChatGroq
from langchain.agents import create_agent

from tools.add_food import add_food
from tools.add_workout import add_workout
from tools.nutrition import extract_nutrition
from tools.summary import daily_summary

from models import UserProfile, Goal, WorkoutType, DietType
from state import DietAgentState


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


tools = [
    add_food,
    add_workout,
    extract_nutrition,
    daily_summary
]


agent = create_agent(
    model=llm,
    tools=tools,
    state_schema=DietAgentState
)


user = UserProfile(
    name="Ganesh",
    age=24,
    sex="Male",
    height_cm=178,
    weight_kg=74,
    goal=Goal.GENERAL_FITNESS,
    workout_type=WorkoutType.GYM,
    diet_type=DietType.NON_VEGETARIAN
)

state = DietAgentState(
    messages=[
        {
            "role": "user",
            "content": "I did a 45 minute chest workout"
        }
    ],
    user=user,
    food_entries=[],
    workout_entries=[],
    nutrition_entries=[],
    date="2026-08-17"
)


if __name__ == "__main__":

    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "I ate 2 eggs for breakfast. Then I did a 45 minute chest workout. Give me my daily summary."
            }
        ],
        **state.model_dump()
    })

    for message in response["messages"]:
        print("\n---")
        print(message)