def route_based_on_confidence(state):
    confidence = state.get("confidence")

    if confidence is None or confidence < 0.6:
        return "escalate"

    return "end"
