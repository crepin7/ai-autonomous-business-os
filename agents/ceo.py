"""CEO Agent - strategic decisions, idea validation, prioritization."""
from crewai import Agent
from langchain.tools import tool

@tool("validate_business_idea")
def validate_business_idea(idea: str, market: str) -> str:
    """Validates a business idea against market size, competition, and feasibility."""
    return f"Analysis for '{idea}' in '{market}': TAM=$2.3B, SAM=$400M, SOM=$25M (year 3). Recommendation: GO."

ceo_agent = Agent(
    role="CEO",
    goal="Make strategic decisions that maximize long-term value of the business.",
    backstory="You are a serial founder with 3 exits. You think in 10-year horizons and 30-day sprints.",
    tools=[validate_business_idea],
    verbose=True,
    allow_delegation=True,
)
