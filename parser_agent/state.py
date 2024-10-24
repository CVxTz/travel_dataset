from pydantic import BaseModel
from typing import Annotated, Optional
from langgraph.graph.message import add_messages

from langchain_core.messages import AnyMessage

from parser_agent.dataset_model import PageType


class OverallState(BaseModel):
    page_content: str
    page_summary: str
    page_type: PageType = PageType.unknown
    messages: Annotated[list[AnyMessage], add_messages] = []
