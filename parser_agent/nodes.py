from enum import Enum

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.graph import END, START

from parser_agent.clients import client_medium, client_large
from parser_agent.dataset_model import Page, page_example, Cities, city_example, Attractions
from parser_agent.state import OverallState


class NodeNames(str, Enum):
    predict_page_type = "predict_page_type"
    parse_city = "parse_city"
    parse_attraction = "parse_attraction"
    end = END
    start = START


def predict_page_type(state: OverallState) -> dict:
    messages = [
        SystemMessage(
            content=f"You are a helpful assistant that outputs in JSON. Follow this schema"
            f" {Page.model_json_schema()}"
        ),
        HumanMessage(content="Give me an example Json of such output"),
        AIMessage(content=page_example.model_dump_json()),
        HumanMessage(content=f"What is the type of this page?\n {state.page_summary}"),
    ]

    local_client = client_medium.with_structured_output(Page)

    page = local_client.invoke(messages)

    return {"page_type": page.page_type}


def parse_city_type(state: OverallState) -> dict:
    messages = [
        SystemMessage(
            content=f"You are a helpful assistant that outputs in JSON. Follow this schema"
            f" {Cities.model_json_schema()}. Only answer with information from the context. "
            f"Keep missing information empty."
        ),
        HumanMessage(content="Give me an example Json of such output"),
        AIMessage(content=Cities(cities=[city_example]).model_dump_json()),
        HumanMessage(content=f"What are the cities mentioned in this page?\n {state.page_content}"),
    ]

    local_client = client_medium.with_structured_output(Cities)

    cities = local_client.invoke(messages)

    return {"cities": cities}

def parse_attractions_type(state: OverallState) -> dict:
    messages = [
        SystemMessage(
            content=f"You are a helpful assistant that outputs in JSON. Follow this schema"
            f" {Cities.model_json_schema()}. Only answer with information from the context. "
            f"Keep missing information empty."
        ),
        HumanMessage(content="Give me an example Json of such output"),
        AIMessage(content=Cities(cities=[city_example]).model_dump_json()),
        HumanMessage(content=f"What are the attractions mentioned in this page?\n {state.page_content}"),
    ]

    local_client = client_medium.with_structured_output(Attractions)

    attractions = local_client.invoke(messages)

    return {"attractions": attractions}

if __name__ == "__main__":
    page_content = "El Jadida (Arabic: الجديدة, romanized: al-Jadīda, [alʒadiːda]) is a major port city on the Atlantic coast of Morocco, located 96 kilometres (60 mi) south of the city of Casablanca, in the province of El Jadida and the region of Casablanca-Settat.[5][6] It has a population of 170,956 as of 2023.[7][unreliable source]The fortified city, built by the Portuguese at the beginning of the 16th century and named Mazagan (Mazagão in Portuguese), was given up by the Portuguese in 1769 and incorporated into Morocco. El Jadida's old city sea walls are one of the Seven Wonders of Portuguese Origin in the World.[8] The Portuguese Fortified City of Mazagan was registered as a UNESCO World Heritage Site in 2004, on the basis of its status as an \"outstanding example of the interchange of influences between European and Moroccan cultures\" and as an \"early example of the realisation of the Renaissance ideals integrated with Portuguese construction technology\". According to UNESCO,[9] the most important buildings from the Portuguese period are the cistern and the Church of the Assumption, both in a Manueline style.[10]The city is a popular resort and destination for both Moroccan and international tourists.[11][12] An important industrial complex, Jorf Lasfar, lies 20 kilometres to the south.[13] Coordinates: 33°14′N 8°30′W "
    _state = OverallState(page_content=page_content, page_summary=page_content[:200])

    print(parse_city_type(_state))
