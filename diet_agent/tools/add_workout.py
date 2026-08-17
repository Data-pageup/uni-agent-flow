from models import WorkoutEntry
from state import DietAgentState
from langchain.tools import tool


@tool
def add_workout(state: DietAgentState, workout: WorkoutEntry) -> DietAgentState:
    """Add a workout entry to the user's daily workout log."""
    state.workout_entries.append(workout)
    return state