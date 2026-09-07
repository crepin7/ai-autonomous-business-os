"""Support Agent - 24/7 ticket handling."""
from crewai import Agent
from langchain.tools import tool

@tool("reply_to_ticket")
def reply_to_ticket(ticket_id: str, message: str) -> str:
    """Sends a reply to a support ticket."""
    return f"Replied to ticket #{ticket_id}"

support_agent = Agent(
    role="Support Lead",
    goal="Resolve 95% of tickets without human escalation, CSAT > 4.7/5.",
    backstory="You are a customer-obsessed support pro with empathy as a superpower.",
    verbose=True,
)
