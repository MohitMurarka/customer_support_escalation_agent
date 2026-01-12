from langchain_core.messages import SystemMessage, HumanMessage
from schemas import ClassificationOutput


def classify_issue(state: dict, llm):
    structured_llm = llm.with_structured_output(ClassificationOutput)

    messages = [
        SystemMessage(
            content=(
                "You are a customer support classifier.\n"
                "Classify the issue into category and urgency."
            )
        ),
        HumanMessage(content=state["user_issue"]),
    ]

    result = structured_llm.invoke(messages)

    return {
        "category": result.category,
        "urgency": result.urgency,
    }
