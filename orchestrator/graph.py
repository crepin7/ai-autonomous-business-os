"""Orchestrator - coordinates all 6 agents via LangGraph."""
from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.ceo import ceo_agent
from agents.marketing import marketing_agent
from agents.engineering import engineering_agent
from agents.sales import sales_agent
from agents.support import support_agent
from agents.finance import finance_agent

class BusinessState(TypedDict):
    idea: str
    market: str
    stage: str
    mrr: float
    logs: list

def ceo_node(state: BusinessState) -> BusinessState:
    result = ceo_agent.run(f"Validate: {state['idea']} in {state['market']}")
    state["stage"] = "validated"
    state["logs"].append(f"CEO: {result}")
    return state

def marketing_node(state: BusinessState) -> BusinessState:
    result = marketing_agent.run(f"Plan launch for {state['idea']}")
    state["logs"].append(f"Marketing: {result}")
    return state

def engineering_node(state: BusinessState) -> BusinessState:
    result = engineering_agent.run(f"Build MVP for {state['idea']}")
    state["stage"] = "built"
    state["logs"].append(f"Engineering: {result}")
    return state

workflow = StateGraph(BusinessState)
workflow.add_node("ceo", ceo_node)
workflow.add_node("marketing", marketing_node)
workflow.add_node("engineering", engineering_node)
workflow.add_edge("ceo", "marketing")
workflow.add_edge("marketing", "engineering")
workflow.set_entry_point("ceo")
workflow.set_finish_point("engineering")

app = workflow.compile()
