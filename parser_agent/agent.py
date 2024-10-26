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
    from devtools import pprint
    from langchain_community.document_loaders import WikipediaLoader

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
    docs = WikipediaLoader(query="Tourism in Paris", load_max_docs=1).load()

    page_title = docs[0].metadata["title"]
    page_content = docs[0].page_content[:4000]
    initial_state = OverallState(page_title=page_title, page_content=page_content)

    final_state_dict = app.invoke(initial_state)

    final_state = OverallState(**final_state_dict)

    pprint(final_state.cities)
    pprint(final_state.attractions)
