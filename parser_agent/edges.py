from parser_agent.dataset_model import PageType
from parser_agent.nodes import NodeNames
from parser_agent.state import OverallState


def parse_city_edge(state: OverallState) -> NodeNames:
    if state.page_type == PageType.city:
        return NodeNames.parse_city
    else:
        return NodeNames.end

def parse_attraction_edge(state: OverallState) -> NodeNames:
    if state.page_type in [PageType.city, PageType.attraction, PageType.country]:
        return NodeNames.parse_attraction
    else:
        return NodeNames.end



if __name__ == "__main__":
    _state = OverallState(page_content="", page_summary="", page_type=PageType.city)

    print(parse_city_edge(_state)) # returns NodeNames.parse_city

