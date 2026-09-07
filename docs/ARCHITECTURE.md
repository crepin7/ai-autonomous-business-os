# ABOS — Technical Architecture

## High-level flow
1. Founder submits idea via `/launch` endpoint.
2. Orchestrator (LangGraph) routes to CEO-Agent first.
3. CEO validates idea -> triggers Marketing + Engineering in parallel.
4. Sales, Support, Finance agents activate once MVP is deployed.
5. Finance-Agent books revenue, pays founder weekly via Stripe Connect.

## Why multi-agent?
- **Better quality** (specialization > generalization)
- **Easier scaling** (add a new agent without retraining the whole system)
- **Clearer accountability** (one agent = one KPI)

## Why LangGraph?
- Stateful, graph-based orchestration
- Built-in retries, fallbacks, human-in-the-loop hooks
- Easy to visualize agent flows in LangSmith

## Cost structure
| Component | Monthly cost |
|---|---|
| LLM API (GPT-4o) | $1,200 |
| Vercel Pro | $20 |
| Postgres + Redis (managed) | $50 |
| Stripe fees | 2.9% of revenue |
| **Total @ 100 businesses** | **~$1,500/mo + rev share** |
