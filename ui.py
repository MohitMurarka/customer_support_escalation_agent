import streamlit as st
from graph import build_graph

from langchain_openai import ChatOpenAI


# ---------- Page Config ----------
st.set_page_config(page_title="Customer Support AI", page_icon="🎧", layout="centered")

st.title("🎧 Customer Support Escalation Agent")
st.caption("LangGraph-based multi-agent support system")

# ---------- LLM ----------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

graph = build_graph(llm)

# ---------- User Input ----------
user_issue = st.text_area(
    "Describe your issue",
    placeholder="Example: I was charged twice for my subscription and need a refund urgently",
)

run_button = st.button("Get Support")

# ---------- Run Agent ----------
if run_button and user_issue.strip():
    with st.spinner("Analyzing your issue..."):
        final_state = graph.invoke({"user_issue": user_issue})

    st.subheader("💬 Support Response")
    st.write(final_state["response"])

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Category", final_state.get("category", "-"))

    with col2:
        st.metric("Urgency", final_state.get("urgency", "-"))

    with col3:
        confidence = final_state.get("confidence")
        if confidence is not None:
            st.metric("Confidence", f"{confidence:.2f}")
        else:
            st.metric("Confidence", "N/A")

    st.divider()

    # ---------- Escalation Status ----------
    escalated = confidence is None or confidence < 0.6

    if escalated:
        st.error("🚨 Escalated to Human Support")
    else:
        st.success("✅ Resolved by AI Agent")
