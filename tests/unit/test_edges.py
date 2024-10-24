from parser_agent.dataset_model import PageType
from parser_agent.nodes import NodeNames
from parser_agent.state import OverallState
from parser_agent.edges import parse_city_edge, parse_attraction_edge


def test_parse_city_edge_city_page():
    """Test when the page type is city."""
    state = OverallState(page_content="", page_summary="", page_type=PageType.city)
    assert parse_city_edge(state) == NodeNames.parse_city


def test_parse_city_edge_non_city_page():
    """Test when the page type is not city."""
    state = OverallState(page_content="", page_summary="", page_type=PageType.other) # Use a different PageType
    assert parse_city_edge(state) == NodeNames.end


def test_parse_attraction_edge_city_page():
    """Test when the page type is city."""
    state = OverallState(page_content="", page_summary="", page_type=PageType.city)
    assert parse_attraction_edge(state) == NodeNames.parse_attraction

