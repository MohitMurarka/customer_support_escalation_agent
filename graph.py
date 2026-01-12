from langgraph.graph import StateGraph, END
from state import SupportState

from nodes.classifier import classify_issue
from nodes.resolver import resolve_issue
from nodes.confidence import evaluate_confidence
from nodes.escalate import escalate_to_human
from routing import route_based_on_confidence
from dotenv import load_dotenv 


load_dotenv(dotenv_path=".env", override=True)

def build_graph(llm):
    graph = StateGraph(SupportState)
    
    graph.add_node("classifier", lambda s: classify_issue(s, llm))
    graph.add_node("resolver", lambda s: resolve_issue(s, llm))
    graph.add_node("confidence", lambda s: evaluate_confidence(s, llm))
    graph.add_node("escalate", escalate_to_human)
    
    graph.set_entry_point("classifier")

    graph.add_edge("classifier", "resolver")
    graph.add_edge("resolver", "confidence")
    
    graph.add_conditional_edges(
        "confidence",
        route_based_on_confidence,
        {
            "escalate": "escalate",
            "end": END
        }
    )
    
    graph.add_edge("escalate", END)

    return graph.compile()