from parser_agent.dataset_model import PageType
from parser_agent.nodes import NodeNames
from parser_agent.state import OverallState
from parser_agent.logger import logger


def parse_city_edge(state: OverallState) -> NodeNames:
    logger.info(f"Entering parse_city_edge function. Current state: {state}") #Added log
    if state.page_type == PageType.city:
        logger.debug(f"Routing to node={NodeNames.parse_city.value}")
        return NodeNames.parse_city.value
    else:
        logger.debug(f"Routing to node={NodeNames.end.value}")
        return NodeNames.end.value


def parse_attraction_edge(state: OverallState) -> NodeNames:
    logger.info(f"Entering parse_attraction_edge function. Current state: {state}") #Added log
    if state.page_type in [PageType.city, PageType.attraction, PageType.country]:
        logger.debug(f"Routing to node={NodeNames.parse_attraction.value}") #Added log
        return NodeNames.parse_attraction.value
    else:
        logger.debug(f"Routing to node={NodeNames.end.value}") #Added log
        return NodeNames.end.value


if __name__ == "__main__":
    _state = OverallState(page_title="", page_content="", page_type=PageType.city)

    print(parse_city_edge(_state))  # returns NodeNames.parse_city
    print(parse_attraction_edge(_state)) #Added test case and log