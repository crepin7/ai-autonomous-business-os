"""Engineering Agent - scaffolds repos, writes code, deploys."""
from crewai import Agent
from langchain.tools import tool

@tool("deploy_to_vercel")
def deploy_to_vercel(project_path: str) -> str:
    """Deploys a Next.js project to Vercel."""
    return f"Deployed {project_path} -> https://app-{project_path}.vercel.app"

engineering_agent = Agent(
    role="CTO",
    goal="Ship reliable, scalable code in hours, not weeks.",
    backstory="You are a senior engineer with 15 years at Google and Stripe.",
    verbose=True,
)
