from parser_agent.dataset_model import PageType
from parser_agent.nodes import predict_page_type
from parser_agent.state import OverallState


def test_predict_page_type():
    state = OverallState(page_content="", page_summary="This page is about Marseille")

    node_result = predict_page_type(state)

    assert node_result["page_type"] == PageType.city

    state = OverallState(page_content="", page_summary="This page is about Vietnam")

    node_result = predict_page_type(state)

    assert node_result["page_type"] == PageType.country
