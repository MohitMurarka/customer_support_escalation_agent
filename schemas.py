from pydantic import BaseModel, Field
from typing import Literal


class ClassificationOutput(BaseModel):
    category: Literal["billing", "technical", "general"]
    urgency: Literal["low", "medium", "high"]


class ConfidenceOutput(BaseModel):
    confidence: float = Field(
        ge=0.0, le=1.0, description="Confidence score between 0 and 1"
    )
