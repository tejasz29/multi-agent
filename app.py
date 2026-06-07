import streamlit as st
from database.db import init_db, save_plan, get_plan, mark_completed
from agents.planner import generate_plan
from agents.explainer import explain_topics
from agents.adaptive import get_adaptive_advice
from utils.charts import progress_pie, subject_bar

# ── Init ──────────────────────────────────────────────────
init_db()
st.set_page_config(page_title="Exam Planner AI", page_icon="📚", layout="wide")

# ── Sidebar ───────────────────────────────────────────────
st.sidebar.title("📚 Exam Planner AI")
page = st.sidebar.radio("Navigate", ["Dashboard", "Study Plan", "Explain Topics", "Adaptive Coach"])

SUBJECTS = [
    "Machine Learning",
    "Operating Systems",
    "Microprocessors",
    "Advanced Mathematics",
    "Drone Technology",
    "Environmental Studies",
]

# ── Dashboard ─────────────────────────────────────────────
if page == "Dashboard":
    st.title("📊 Dashboard")
    plan = get_plan()
    if not plan:
        st.info("No study plan yet. Go to **Study Plan** to generate one.")
    else:
        total = len(plan)
        completed = sum(1 for e in plan if e["completed"])
        remaining = total - completed
        pct = round(completed / total * 100) if total else 0

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Sessions", total)
        c2.metric("Completed", completed)
        c3.metric("Remaining", remaining)
        c4.metric("Progress", f"{pct}%")

        col_a, col_b = st.columns(2)
        with col_a:
            st.pyplot(progress_pie(completed, total))
        with col_b:
            fig = subject_bar(plan)
            if fig:
                st.pyplot(fig)
            else:
                st.info("Complete some sessions to see subject-wise stats.")

        # Smart insight
        if pct == 0:
            st.warning("🚨 You haven't started yet. Begin today!")
        elif pct < 40:
            st.error("⚠️ You are behind schedule. Pick up the pace!")
        elif pct < 75:
            st.warning("📌 Stay consistent — you're making progress.")
        else:
            st.success("✅ You're on track! Keep it up.")

# ── Study Plan ────────────────────────────────────────────
elif page == "Study Plan":
    st.title("🗓️ Study Plan Generator")

    selected = st.multiselect("Select Subjects", SUBJECTS, default=SUBJECTS[:4])
    days = st.slider("Study Days Available", 3, 14, 9)

    if st.button("🚀 Generate Plan", type="primary"):
        with st.spinner("Planner Agent is building your schedule..."):
            try:
                plan_data = generate_plan(selected, days)
                save_plan(plan_data)
                st.success("Plan generated and saved!")
            except Exception as e:
                st.error(f"Error: {e}")

    plan = get_plan()
    if plan:
        st.subheader("Your Study Plan")
        for entry in plan:
            col1, col2 = st.columns([5, 1])
            label = f"**Day {entry['day']}** — {entry['subject']}: {entry['topics']}"
            with col1:
                st.markdown(label)
            with col2:
                done = st.checkbox("Done", value=bool(entry["completed"]), key=f"chk_{entry['id']}")
                if done != bool(entry["completed"]):
                    mark_completed(entry["id"], done)
                    st.rerun()

# ── Explainer ─────────────────────────────────────────────
elif page == "Explain Topics":
    st.title("🧠 Topic Explainer")

    plan = get_plan()
    if not plan:
        st.info("Generate a study plan first.")
    else:
        options = {f"Day {e['day']} — {e['subject']}": e for e in plan}
        choice = st.selectbox("Pick a study session to explain", list(options.keys()))
        entry = options[choice]

        if st.button("✨ Explain", type="primary"):
            with st.spinner("Explainer Agent is simplifying concepts..."):
                explanation = explain_topics(entry["subject"], entry["topics"])
                st.markdown(explanation)

# ── Adaptive Coach ────────────────────────────────────────
elif page == "Adaptive Coach":
    st.title("🤖 Adaptive Learning Coach")

    plan = get_plan()
    if not plan:
        st.info("Generate a study plan first.")
    else:
        total_days = max(e["day"] for e in plan)
        completed_entries = [f"Day {e['day']}: {e['subject']} – {e['topics']}" for e in plan if e["completed"]]
        missed_entries    = [f"Day {e['day']}: {e['subject']} – {e['topics']}" for e in plan if not e["completed"]]
        remaining_days = len([e for e in plan if not e["completed"]])

        st.markdown(f"✅ **{len(completed_entries)}** sessions done &nbsp;|&nbsp; ❌ **{len(missed_entries)}** missed &nbsp;|&nbsp; ⏳ **{remaining_days}** remaining")

        if st.button("🎯 Get Adaptive Advice", type="primary"):
            with st.spinner("Adaptive Agent is analyzing your progress..."):
                advice = get_adaptive_advice(completed_entries, missed_entries, remaining_days)
                st.markdown(advice)