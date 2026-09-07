"""Sales Agent - outbound, lead qualification, demos."""
from crewai import Agent
from langchain.tools import tool

@tool("send_cold_email")
def send_cold_email(lead_email: str, subject: str, body: str) -> str:
    """Sends a personalized cold email."""
    return f"Email sent to {lead_email}: '{subject}'"

sales_agent = Agent(
    role="Head of Sales",
    goal="Close 20% of qualified leads within 14 days.",
    backstory="You are a top BDR who has booked $10M+ in pipeline.",
    verbose=True,
)
