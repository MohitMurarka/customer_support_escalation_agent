from langchain_core.messages import SystemMessage, HumanMessage


def resolve_issue(state: dict, llm):

    category = state["category"]
    urgency = state["urgency"]

    system_prompt = f"""
    You are a customer support agent.

    Issue category: {category}
    Urgency: {urgency}

    Guidelines:
    - Be clear and professional
    - If urgency is high, be concise and direct
    - Provide actionable steps
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=state["user_issue"]),
    ]

    result = llm.invoke(messages)

    return {"response": result.content}
