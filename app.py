from graph import build_graph

# ---- Choose ONE LLM ----
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
# ------------------------

graph = build_graph(llm)

user_issue = input("Describe your issue: ")

initial_state = {"user_issue": user_issue}

final_state = graph.invoke(initial_state)

print("\n--- FINAL OUTPUT ---")
print("Response:", final_state["response"])
print("Category:", final_state.get("category"))
print("Urgency:", final_state.get("urgency"))
print("Confidence:", final_state.get("confidence"))
print("Escalated:", final_state.get("escalate"))
