from langchain_groq import ChatGroq
from dotenv import load_dotenv
from app.router_node import router_node

load_dotenv() 

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

messages = [
    (
        "system",
        "You are a helpful assistant tasked with performing arithmetic on a set of inputs",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)

tools = [router_node]

llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)