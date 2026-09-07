"""FastAPI backend for ABOS."""
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from orchestrator.graph import app as orchestrator

api = FastAPI(title="AI Autonomous Business OS")

class LaunchRequest(BaseModel):
    idea: str
    market: str
    founder_email: str

@api.post("/launch")
async def launch_business(req: LaunchRequest, bg: BackgroundTasks):
    """Kick off a new autonomous business."""
    state = {"idea": req.idea, "market": req.market, "stage": "init", "mrr": 0.0, "logs": []}
    bg.add_task(orchestrator.invoke, state)
    return {"status": "launching", "idea": req.idea}

@api.get("/health")
async def health():
    return {"status": "ok", "agents": 6, "market": "open"}
