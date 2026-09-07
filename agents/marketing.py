"""Marketing Agent - SEO, ads, copy, social posts."""
from crewai import Agent
from langchain.tools import tool

@tool("write_ad_copy")
def write_ad_copy(product: str, audience: str, platform: str) -> str:
    """Generates ad copy for the given platform."""
    return f"[{platform} ad for {product} -> {audience}] Stop wasting hours on tasks AI can do in seconds. Try {product} free."

marketing_agent = Agent(
    role="Marketing Lead",
    goal="Drive qualified traffic and signups at <$5 CAC.",
    backstory="You are a growth marketer who has scaled 5 startups from 0 to $1M ARR.",
    verbose=True,
)
