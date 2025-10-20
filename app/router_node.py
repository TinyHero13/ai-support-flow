from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import tools_condition, ToolNode


def router_node(tools, assistant):
    builder = StateGraph(MessagesState, name="RouterNode")

    builder.add_node("assistant", assistant)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "assistant")

    builder.add_conditional_edges(
        "assistant",
        tools_condition,   
        {
            "tools": "tools",   
            "__end__": END,    
        },
    )

    # Volta ao assistant após executar a ferramenta para que ele possa explicar
    builder.add_edge("tools", "assistant")

    return builder.compile()
