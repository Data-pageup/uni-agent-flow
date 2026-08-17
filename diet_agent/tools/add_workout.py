from models import WorkoutEntry
from langchain.tools import tool, ToolRuntime
from state import DietAgentState


@tool
def add_workout(
    workout: WorkoutEntry,
    runtime: ToolRuntime[DietAgentState]
) -> str:
    """Add a workout entry to the user's daily workout log."""

    runtime.state["workout_entries"].append(workout)

    return f"Added {workout.focus.value} workout to today's log."