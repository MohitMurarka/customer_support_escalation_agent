from langchain_core.messages import SystemMessage, HumanMessage
from schemas import ConfidenceOutput


def evaluate_confidence(state: dict, llm):
    structured_llm = llm.with_structured_output(ConfidenceOutput)

    system_prompt = """
    You are a quality assurance agent.
    Evaluate how well the assistant's response resolves the user's issue.
    """

    review_input = f"""
    User issue:
    {state["user_issue"]}

    Assistant response:
    {state["response"]}

    Urgency:
    {state.get("urgency")}
    """

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=review_input),
    ]

    result = structured_llm.invoke(messages)

    return {
        "confidence": result.confidence
    }
