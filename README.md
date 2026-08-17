# AI Diet & Fitness Agent

> Natural Language → Tool Calling → Structured State → Nutrition Intelligence

An AI-powered Diet & Fitness Agent that lets you log food and workouts, retrieve nutrition data, and get a daily summary — just by talking to it naturally.

```
"I ate 2 eggs for breakfast and then did a 45 minute chest workout. Give me today's summary."
```

**Status:** Phase 1 — Core Agent System ✅

---

## ✨ What it does

Instead of manually filling forms, you describe what you ate or did, and the agent:

1. Understands the request (LLM reasoning)
2. Decides which tool(s) to call
3. Updates a structured, validated application state
4. Retrieves real nutrition data from the web
5. Generates a clean daily summary

```
User → Natural Language → LLM Agent → Tool Selection
     → Structured State → Nutrition/Workout/Food Data
     → Daily Summary
```

---

## 🧱 Tech Stack

| Component   | Purpose                                                   |
|-------------|------------------------------------------------------------|
| **Python**  | Core language                                              |
| **Pydantic**| Structured, validated data models                          |
| **LangChain** | LLM integration, tool creation, structured output, agent creation |
| **LangGraph** | Agent state management & tool execution under the hood   |
| **Groq**    | LLM provider (current model: `openai/gpt-oss-120b`)         |
| **Tavily**  | Web search for nutrition information                        |
| **python-dotenv** | Loads API keys from `.env`                             |

> **Model note:** `llama-3.3-70b-versatile` was dropped (became unavailable) and `qwen/qwen3.6-27b` was dropped (too much reasoning overhead for simple tool calls). Currently using `openai/gpt-oss-120b` for clean tool-calling behavior.

---

## 📁 Project Structure

```
diet_agent/
│
├── agent/
│   └── diet_agent.py        # Agent wiring (LLM + tools)
│
├── tools/
│   ├── add_food.py          # Logs a FoodEntry into state
│   ├── add_workout.py       # Logs a WorkoutEntry into state
│   ├── nutrition.py         # Tavily search + Groq structured extraction
│   └── summary.py           # Builds the daily summary
│
├── models.py                 # Pydantic models (UserProfile, FoodEntry, etc.)
├── state.py                  # DietAgentState definition
└── main.py                   # Example / manual test entry point
```

> Structure will evolve as the project grows (FastAPI backend + UI planned).

---

## 🗃️ Data Models

All data is modeled with **Pydantic** instead of raw dictionaries.

- **`UserProfile`** — `name`, `age`, `sex`, `height_cm`, `weight_kg`, `goal`, `workout_type`, `diet_type`
- **`FoodEntry`** — `food_name`, `quantity`, `unit`, `time`
- **`WorkoutEntry`** — `focus`, `duration`, `unit`, `time` (defaults to `"now"`)
- **`NutritionInfo`** — `food_name`, `calories`, `protein_g`, `carbs_g`, `fat_g`
- **`DietAgentState`** — `messages`, `user`, `food_entries`, `workout_entries`, `nutrition_entries`, `date`

---

## 🔧 Tools

| Tool | Description |
|---|---|
| `add_food` | Logs a `FoodEntry` into `state["food_entries"]` via `runtime.state` |
| `add_workout` | Logs a `WorkoutEntry` into `state["workout_entries"]` via `runtime.state` |
| `extract_nutrition` | Tavily search → raw nutrition text → Groq structured extraction → `NutritionInfo` |
| `daily_summary` | Reads state and produces a formatted daily report |

**Key design decision:** tools read/write the *real* application state via `runtime.state` rather than letting the LLM construct state itself. This prevents the model from inventing user data (see [Architecture Notes](#-architecture-notes) below).

---

## 🚀 Getting Started

### 1. Clone & install dependencies

```bash
git clone <your-repo-url>
cd diet_agent
pip install -r requirements.txt
```

### 2. Set up environment variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 3. Run

Run as a module (not as a script) to avoid import errors:

```bash
python -m agent.diet_agent
```

Or run the example flow in `main.py`:

```bash
python main.py
```

---

## 💡 Example

**Input:**
```
I ate 2 eggs for breakfast. Then I did a 45 minute chest workout. Give me my daily summary.
```

**Flow:**
```
User → LLM → add_food → extract_nutrition → add_workout → daily_summary → Final response
```

**Output:**
```
Date: 2026-08-17

Food consumed:
- eggs: 2 pieces at now

Nutrition:
- Calories: 77.50 kcal
- Protein: 6.30 g
- Carbs: 0.56 g
- Fat: 5.30 g

Workouts:
- Chest: 45 minutes at now
```

---

## 🏗️ Architecture Notes

Early versions let the LLM generate the *entire* application state, which caused it to hallucinate user data (fake names, ages, weights). This was fixed by restructuring the flow so the **real application state drives the tools**, and the LLM only supplies the minimal arguments a tool needs:

```
REAL APPLICATION STATE → Agent Runtime → Tools
```

Tools then read/write state through `runtime.state`, e.g. `runtime.state["food_entries"]`, while individual entries remain typed Pydantic objects (`food.food_name`).

---

## ✅ Tested So Far

- Food logging (`add_food`)
- Workout logging (`add_workout`)
- Nutrition retrieval (Tavily) + structured extraction (Groq → `NutritionInfo`)
- Daily summary generation
- End-to-end multi-tool orchestration

## 🚧 Roadmap

- [ ] Fix nutrition quantity handling (e.g. "2 eggs" should scale nutrition, not default to 1 egg)
- [ ] Persistent storage (SQLite)
- [ ] Conversational memory across turns
- [ ] Nutrition calculations: BMR, TDEE, calorie/macro targets
- [ ] Progress tracking (target vs. consumed vs. remaining)
- [ ] AI-generated personalized recommendations
- [ ] FastAPI backend + Streamlit/web UI

---

## 📄 Documentation

Full project documentation (architecture diagrams, data models, problem log) is available as a PDF: `diet_agent_documentation.pdf` (LaTeX source: `diet_agent_documentation.tex`).

---

## 👤 Author

**Amirtha Ganesh R.**
