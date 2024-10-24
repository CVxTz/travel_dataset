from typing import Annotated, Optional

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from pydantic import BaseModel

from parser_agent.dataset_model import PageType, Cities, Attractions


class OverallState(BaseModel):
    page_content: str
    page_summary: str
    page_type: PageType = PageType.unknown
    cities: Optional[Cities] = None
    attractions: Optional[Attractions] = None
    messages: Annotated[list[AnyMessage], add_messages] = []
