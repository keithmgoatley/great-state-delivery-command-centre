import numpy as np, pandas as pd

def get_portfolio_status():
    return pd.DataFrame([
        {"Client": "Global Retail Group", "Project": "E-Commerce Platform Replatforming", "Phase": "Build & Integrate", "RAG": "Amber", "Budget_Total": 450000, "Budget_Burned": 280000, "Completion": 0.60},
        {"Client": "FinTech Innovators", "Project": "Mobile App MVP Launch", "Phase": "UAT & QA", "RAG": "Green", "Budget_Total": 120000, "Budget_Burned": 105000, "Completion": 0.90},
        {"Client": "Public Sector Dept", "Project": "Legacy Portal Migration", "Phase": "Discovery & Strategy", "RAG": "Green", "Budget_Total": 85000, "Budget_Burned": 15000, "Completion": 0.15},
        {"Client": "Healthcare Provider", "Project": "Patient Dashboard App", "Phase": "Design & Prototyping", "RAG": "Red", "Budget_Total": 180000, "Budget_Burned": 95000, "Completion": 0.35}
    ])

def get_sprint_tasks():
    return pd.DataFrame([
        {"Discipline": "UX/UI Design", "Task": "Finalize Checkout Flow wireframes", "Assignee": "Design Team", "Status": "Done", "Sprint": "Sprint 14"},
        {"Discipline": "Frontend Dev", "Task": "Implement React components for Dashboard", "Assignee": "Engineering", "Status": "In Progress", "Sprint": "Sprint 14"},
        {"Discipline": "Backend Dev", "Task": "Payment Gateway API Integration", "Assignee": "Engineering", "Status": "Blocked", "Sprint": "Sprint 14"},
        {"Discipline": "QA / Testing", "Task": "Regression testing on staging environment", "Assignee": "QA Team", "Status": "To Do", "Sprint": "Sprint 14"},
        {"Discipline": "Strategy", "Task": "Client stakeholder alignment workshop", "Assignee": "Delivery Manager", "Status": "In Progress", "Sprint": "Sprint 14"}
    ])

def get_ai_risks():
    return pd.DataFrame([
        {"Risk_ID": "RSK-01", "Project": "Patient Dashboard App", "Category": "Commercial/Scope", "Description": "Client requesting additional reporting views outside of MVP scope.", "Probability": "High", "Impact": "High", "AI_Mitigation": "AI Suggests: Trigger Change Request (CR) workflow immediately. Do not pause current sprint. Isolate new requirements into Phase 2 backlog and present cost impact to client tomorrow."},
        {"Risk_ID": "RSK-02", "Project": "E-Commerce Platform Replatforming", "Category": "Technical", "Description": "Third-party inventory API latency causing timeout errors on staging.", "Probability": "Medium", "Impact": "High", "AI_Mitigation": "AI Suggests: Allocate 1 Backend Eng to implement caching layer/circuit breaker pattern. Log dependency risk in client governance report."}
    ])
