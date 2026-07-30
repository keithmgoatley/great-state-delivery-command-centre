import streamlit as st, pandas as pd, plotly.graph_objects as go, plotly.express as px
import data as D

st.set_page_config(page_title="Digital Delivery Command Centre", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #0a0a0a; color: #f5f5f5; }
h1 { background: linear-gradient(90deg, #ff4b4b, #ff8f00); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800; letter-spacing: -1px; }
h2, h3 { color: #ffffff; font-weight: 600; }
div[data-testid="metric-container"] { background: #171717; border: 1px solid #262626; border-radius: 8px; padding: 1.2rem; }
[data-testid="stMetricValue"] { font-size: 2rem !important; font-weight: 800; color: #ffffff !important; }
[data-testid="stMetricLabel"] { color: #a3a3a3 !important; text-transform: uppercase; font-size: 0.75rem !important; letter-spacing: 1px; }
.stTabs [data-baseweb="tab-list"] { background: #171717; border-radius: 8px; border: 1px solid #262626; padding: 6px; }
.stTabs [data-baseweb="tab"] { color: #a3a3a3; }
.stTabs [aria-selected="true"] { background: rgba(255, 75, 75, 0.15) !important; color: #ff4b4b !important; border-bottom: none !important; }
.ai-box { background: rgba(255, 143, 0, 0.1); border-left: 4px solid #ff8f00; padding: 15px; border-radius: 0 8px 8px 0; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

PLOT_BG = dict(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="#a3a3a3"))

port_df = D.get_portfolio_status()
sprint_df = D.get_sprint_tasks()
risk_df = D.get_ai_risks()

st.title("Great State: Digital Delivery Command Centre")
st.markdown("<p style='color:#a3a3a3; font-size:1.05rem; margin-bottom: 2rem;'>Bringing structure to complexity. Real-time commercial governance, multi-disciplinary sprint tracking, and AI-powered risk mitigation for enterprise digital projects.</p>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Active Projects", len(port_df), "Agency Portfolio")
c2.metric("Total Managed Budget", f"£{port_df['Budget_Total'].sum():,}", "Commercial Pacing")
c3.metric("Blocked Tasks", len(sprint_df[sprint_df["Status"] == "Blocked"]), "Requires Unblocking")
c4.metric("Active Risks (RAG: Red/Amber)", len(port_df[port_df["RAG"].isin(["Red", "Amber"])]), "Requires Mitigation")

t1, t2, t3 = st.tabs(["Commercial Governance & RAG", "Multi-Disciplinary Sprint Tracker", "AI Risk Mitigation Console"])

with t1:
    st.markdown("### Portfolio Budget Burn vs. Delivery Progress")
    fig = go.Figure()
    for idx, row in port_df.iterrows():
        color = "#10b981" if row["RAG"] == "Green" else ("#f59e0b" if row["RAG"] == "Amber" else "#ef4444")
        fig.add_trace(go.Indicator(
            mode = "number+gauge", value = row["Budget_Burned"],
            title = {'text': f"<span style='color:white;font-size:16px;'>{row['Project']}</span><br><span style='color:{color};font-size:12px;'>RAG: {row['RAG']} | {row['Completion']:.0%} Complete</span>"},
            gauge = {
                'shape': "bullet", 'axis': {'range': [None, row["Budget_Total"] * 1.1]},
                'threshold': {'line': {'color': "red", 'width': 2}, 'thickness': 0.75, 'value': row["Budget_Total"]},
                'steps': [{'range': [0, row["Budget_Total"]], 'color': "rgba(255,255,255,0.1)"}],
                'bar': {'color': color}
            },
            domain = {'x': [0.1, 1], 'y': [1 - (idx+1)*0.25, 1 - idx*0.25 - 0.05]}
        ))
    fig.update_layout(height=400, margin=dict(t=30, b=10, l=10, r=10), **PLOT_BG)
    st.plotly_chart(fig, use_container_width=True)

with t2:
    st.markdown("### Active Sprint: Cross-Functional Delivery")
    st.dataframe(sprint_df.style.map(lambda v: "color:#ef4444; font-weight:bold" if v == "Blocked" else ("color:#10b981" if v == "Done" else "color:#a3a3a3"), subset=["Status"]), use_container_width=True, hide_index=True)

with t3:
    st.markdown("### AI-Assisted Risk & Issue Mitigation")
    for _, row in risk_df.iterrows():
        st.markdown(f"""
        <div class='ai-box'>
            <h4 style='color:#ff8f00; margin:0;'>⚠️ {row['Project']} - {row['Category']} Risk</h4>
            <p style='margin:5px 0 10px 0;'><b>Issue:</b> {row['Description']} (Probability: {row['Probability']} | Impact: {row['Impact']})</p>
            <p style='margin:0; font-family:monospace; color:#e5e5e5;'>{row['AI_Mitigation']}</p>
        </div>
        """, unsafe_allow_html=True)
