from typing_extensions import TypedDict,Annotated
from typing import Literal,Optional

class SupportState(TypedDict) : 
    user_issue : str
    
    category  : Annotated[
        Optional[Literal["billing","technical","general"]],
        "Type of support issue."
    ]
    
    urgency : Annotated[
        Optional[Literal["low", "medium", "high"]],
        "Urgency level of the issue."
    ]
    
    response: Optional[str]

    confidence: Optional[float]

    escalate: Optional[bool]
