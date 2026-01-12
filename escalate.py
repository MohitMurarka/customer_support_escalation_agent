def escalate_to_human(state: dict):
    return {
        "response": (
            "Your issue requires human assistance. "
            "A support agent will contact you shortly."
        )
    }
