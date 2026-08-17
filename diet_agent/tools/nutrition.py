import os
from tavily import TavilyClient
from dotenv import load_dotenv
from models import NutritionInfo

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

tavily = TavilyClient(api_key=TAVILY_API_KEY)


def search_nutrition(food: str):
    """Search for nutritional information about a food."""

    response = tavily.search(
        query=f"{food} nutrition calories protein carbohydrates fat",
        search_depth="advanced",
        max_results=2
    )

    return response["results"]







llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a nutrition information extractor.

        From the provided food information, extract ONLY:
        - food name
        - calories
        - protein in grams
        - carbohydrates in grams
        - fat in grams

        Ignore all other information.
        If multiple sources provide values, choose the most reliable
        and reasonable value."""
    ),
    (
        "human",
        "{food_data}"
    )
])

structured_llm = prompt | llm.with_structured_output(NutritionInfo)


def extract_nutrition(food: str):
    results = search_nutrition(food)

    food_data = "\n\n".join(
        result["content"] for result in results
    )

    nutrition = structured_llm.invoke({
        "food_data": food_data
    })

    return nutrition



if __name__ == "__main__":
    nutrition = extract_nutrition("2 eggs")
    print(nutrition)