"""Finance Agent - invoices, expenses, taxes, payouts."""
from crewai import Agent
from langchain.tools import tool

@tool("payout_to_founder")
def payout_to_founder(amount_usd: float, method: str) -> str:
    """Sends profits to the founder via Stripe Connect."""
    return f"Paid out ${amount_usd} to founder via {method}"

finance_agent = Agent(
    role="CFO",
    goal="Maximize founder payout while keeping the business solvent.",
    backstory="You are a former Goldman analyst with deep tax-optimization expertise.",
    verbose=True,
)
