from typing import Optional

from pydantic import BaseModel, computed_field

from parser_agent.dataset_model import Attractions, Cities, PageType


class OverallState(BaseModel):
    page_title: str
    page_content: str
    page_type: PageType = PageType.unknown
    cities: Optional[Cities] = None
    attractions: Optional[Attractions] = None
    url: Optional[str] = None
    # messages: Annotated[list[AnyMessage], add_messages] = []

    @computed_field
    @property
    def page_summary(self) -> str:
        return f"{self.page_title} {self.page_content[:400]}"
