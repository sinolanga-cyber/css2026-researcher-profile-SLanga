import streamlit as st
import time
import random

st.set_page_config(page_title="Researcher Profile", page_icon="🧠", layout="centered")

# --- Simple creative styling ---
st.markdown("""
<style>
.hero{
  padding:18px 18px;
  border-radius:18px;
  background: linear-gradient(135deg, rgba(99,102,241,0.22), rgba(16,185,129,0.16));
  border: 1px solid rgba(255,255,255,0.12);
}
.badge{
  display:inline-block;
  padding:6px 10px;
  margin:4px 6px 0 0;
  border-radius:999px;
  border:1px solid rgba(255,255,255,0.14);
  background: rgba(255,255,255,0.05);
  font-size:0.92rem;
}
.card{
  padding:12px 14px;
  border-radius:16px;
  border: 1px solid rgba(255,255,255,0.10);
  background: rgba(255,255,255,0.03);
  margin: 10px 0;
}
.small{opacity:0.85;}
</style>
""", unsafe_allow_html=True)

def badges(items):
    st.markdown("".join([f"<span class='badge'>{x}</span>" for x in items]), unsafe_allow_html=True)

# --- Header / Hero ---
st.markdown("""
<div class="hero">
  <h1 style="margin:0;">Sinovuyo Langa — Research Profile</h1>
  <p class="small" style="margin:8px 0 0 0;">
    I am a seasoned business process and data enablement professional with 9+ years of experience
    in business intelligence and process improvement.
  </p>
</div>
""", unsafe_allow_html=True)

st.write("")

#Mini navigation (simple + creative)
tab = st.radio("Choose a section 👇", ["Research", "Projects", "Publications", "Contact"], horizontal=True)

#Research
if tab == "Research":
    st.header("Implementing AI-Powered Blockchain Technology in South Africa's Tender System")

    pillars = [
        "Project Approach: Adoption of New Technology",
        "Technology Taxonomy Analysis",
        "Environmental Protection & Sustainable Procurement",
    ]
    badges(pillars)

    st.write("")
    st.subheader("Build a quick concept (interactive)")

    options = [
        "Smart contracts to enforce tender rules",
        "AI anomaly detection for fraud/red flags",
        "Immutable audit trail for transparency",
        "Explainable scoring for fairness",
        "Privacy controls for sensitive data",
    ]

    picks = st.multiselect("Pick 2–4 components", options, default=options[:2])

    focus = st.slider("Focus: Governance ↔ Innovation", 0, 10, 6)
    speed = st.slider("Automation level", 0, 10, 7)

    if st.button("Generate my concept ✨"):
        with st.spinner("Generating..."):
            time.sleep(0.6)

        tone = "governance-first" if focus <= 4 else "innovation-first" if focus >= 7 else "balanced"
        automation = "high" if speed >= 7 else "moderate" if speed >= 4 else "light"
        one_liner = random.choice([
            "A transparent tender system with built-in trust.",
            "Procurement that’s faster, fairer, and auditable.",
            "From paperwork to proof: decisions you can verify.",
        ])

        st.success(one_liner)
        st.markdown(f"""
<div class="card">
<b>Your concept summary</b><br><br>
<b>Style:</b> {tone}<br>
<b>Automation:</b> {automation}<br><br>
<b>Included components:</b><br>
{"".join([f"• {p}<br>" for p in picks]) if picks else "• (Select at least one component)"}
</div>
""", unsafe_allow_html=True)

#Projects
elif tab == "Projects":
    st.header("Projects / Work")

    projects = [
        {
            "title": "USAID Programme Data & Analytics Modernisation (Panagora Group)",
            "tags": ["Data Quality", "Power BI", "Tableau", "Governance"],
            "text": "Designed data quality frameworks and analytics solutions for multi-region USAID programmes. Built dashboards for donor reporting, created SOPs/data dictionaries, and strengthened governance aligned with DAMA-DMBOK."
        },
        {
            "title": "Humanitarian BI & Data Transparency (UN World Food Programme)",
            "tags": ["Tableau", "SAP BW", "Power BI", "Data Lineage"],
            "text": "Developed regional BI dashboards for operational transparency across multiple countries. Led a data transparency initiative improving lineage, trust, and accessibility; trained country offices on BI tools."
        },
        {
            "title": "Financial & Commercial KPI Dashboards (Sasol – SAP BI)",
            "tags": ["SAP BI", "SQL", "KPI Dashboards", "Migration"],
            "text": "Built and optimised KPI dashboards for budgeting, forecasting, and order lifecycle tracking. Contributed to SAP HANA → Teradata migration to improve performance and scalability."
        },
    ]

    # simple filters
    all_tags = sorted({t for p in projects for t in p["tags"]})
    selected_tags = st.multiselect("Filter by tag (optional)", all_tags)

    for p in projects:
        if selected_tags and not any(t in p["tags"] for t in selected_tags):
            continue

        with st.expander(p["title"]):
            badges(p["tags"])
            st.write(p["text"])

            lens = st.radio("View as", ["Summary", "Impact bullets"], horizontal=True, key=p["title"])
            if lens == "Impact bullets":
                st.write("• Stronger reporting and decision support")
                st.write("• Better data quality and governance")
                st.write("• Clearer stakeholder alignment")

# --- Publications ---
elif tab == "Publications":
    st.header("Publications (optional)")
    st.markdown("""
- Paper 1 (2024) — *Contact me.*  
- Paper 2 (2027) — *In the pipeline.*
""")
    st.info("You can replace these with real titles and links anytime.")

# --- Contact ---
else:
    st.header("Contact")
    st.write("Email: **sinolanga@gmail.com**")

    st.write("")
    st.subheader("Quick message (demo)")
    with st.form("msg"):
        name = st.text_input("Your name")
        message = st.text_area("Message")
        sent = st.form_submit_button("Send ✉️")
        if sent:
            st.success("Message captured (demo). Add email/API later if you want this to really send.")
