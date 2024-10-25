from idlelib.browser import file_open

from langgraph.graph import END, START, StateGraph

from parser_agent.edges import parse_attraction_edge, parse_city_edge
from parser_agent.nodes import (
    NodeNames,
    parse_attractions,
    parse_city,
    predict_page_type,
)
from parser_agent.state import OverallState

workflow = StateGraph(OverallState)

# Add nodes
workflow.add_node(NodeNames.predict_page_type.value, predict_page_type)
workflow.add_node(NodeNames.parse_city.value, parse_city)
workflow.add_node(NodeNames.parse_attraction.value, parse_attractions)


# Add edges
workflow.add_edge(START, NodeNames.predict_page_type.value)
workflow.add_conditional_edges(NodeNames.predict_page_type.value, parse_city_edge)
workflow.add_conditional_edges(NodeNames.predict_page_type.value, parse_attraction_edge)
workflow.add_edge(NodeNames.parse_attraction.value, END)
workflow.add_edge(NodeNames.parse_city.value, END)


app = workflow.compile()

if __name__ == "__main__":
    import io

    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt

    png_bytes = app.get_graph().draw_png()

    # Handle both bytes and file paths
    if isinstance(png_bytes, bytes):
        img = mpimg.imread(io.BytesIO(png_bytes))
    elif isinstance(png_bytes, str):  # Assuming it's a file path
        img = mpimg.imread(png_bytes)
    else:
        raise TypeError(
            "Unexpected type from draw_mermaid_png: {}".format(type(png_bytes))
        )

    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis("off")  # Hide axes
    plt.show()

    # Example Usage
    page_content = 'El Jadida (Arabic: الجديدة, romanized: al-Jadīda, [alʒadiːda]) is a major port city on the Atlantic coast of Morocco, located 96 kilometres (60 mi) south of the city of Casablanca, in the province of El Jadida and the region of Casablanca-Settat.[5][6] It has a population of 170,956 as of 2023.[7][unreliable source]The fortified city, built by the Portuguese at the beginning of the 16th century and named Mazagan (Mazagão in Portuguese), was given up by the Portuguese in 1769 and incorporated into Morocco. El Jadida\'s old city sea walls are one of the Seven Wonders of Portuguese Origin in the World.[8] The Portuguese Fortified City of Mazagan was registered as a UNESCO World Heritage Site in 2004, on the basis of its status as an "outstanding example of the interchange of influences between European and Moroccan cultures" and as an "early example of the realisation of the Renaissance ideals integrated with Portuguese construction technology". According to UNESCO,[9] the most important buildings from the Portuguese period are the cistern and the Church of the Assumption, both in a Manueline style.[10]The city is a popular resort and destination for both Moroccan and international tourists.[11][12] An important industrial complex, Jorf Lasfar, lies 20 kilometres to the south.[13] Coordinates: 33°14′N 8°30′W '
    initial_state = OverallState(page_title="El Jadida", page_content=page_content)

    final_state_dict = app.invoke(initial_state)

    final_state = OverallState(**final_state_dict)

    print(final_state)
