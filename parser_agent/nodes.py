from parser_agent.clients import client_medium
from parser_agent.state import OverallState
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from parser_agent.dataset_model import Page, page_example


def predict_page_type(state: OverallState) -> dict:
    messages = [
        SystemMessage(
            content=f"You are a helpful assistant that outputs in JSON. Follow this schema {Page.model_json_schema()}"
        ),
        HumanMessage(content="Give me an example Json of such output"),
        AIMessage(content=page_example.model_dump_json()),
        HumanMessage(content=f"What is the type of this page?\n {state.page_summary}"),
    ]

    local_client = client_medium.with_structured_output(Page)

    page = local_client.invoke(messages)

    return {"page_type": page.page_type}


if __name__ == "__main__":
    _state = OverallState(page_content="", page_summary="This page is about Marseille")

    print(predict_page_type(_state))
