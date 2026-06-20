from agents.water_agent.tools import (
    get_water_reports,
    get_pending_reports,
    get_resolved_reports,
    get_summary,
)

try:
    from google.adk.agents import Agent

    root_agent = Agent(
        name="water_leakage_agent",
        model="gemini-2.0-flash",
        description="Smart Water Leakage Management Agent",
        instruction="""
You are an intelligent water leakage management assistant.

Your responsibilities:

- Analyze water leakage reports
- Provide report summaries
- Give pending and resolved statistics
- Help administrators understand civic water issues
- Use available tools whenever needed

Always provide concise and accurate responses.
""",
        tools=[
            get_water_reports,
            get_pending_reports,
            get_resolved_reports,
            get_summary,
        ],
    )

except Exception:
    root_agent = None