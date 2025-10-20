from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import MessagesState
from app.router_node import router_node
from app.faq_node import faq_node
from app.ticket_node import ticket_node

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
)

tools = [faq_node, ticket_node]

llm_with_tools = llm.bind_tools(tools)

def assistant(state: MessagesState):
    sys_msg = {
        "role": "system",
        "content": "Você é um assistente útil que decide quando usar ferramentas ou responder diretamente."
    }
    response = llm_with_tools.invoke([sys_msg] + state["messages"])
    return {"messages": [response]}

graph = router_node(tools, assistant)

def send_message(text: str):
    initial_state = {"messages": [("human", text)]}
    result = graph.invoke(initial_state)

    for i, msg in enumerate(result["messages"]):
        print(f"\nMensagem {i+1}:")
        print(f"Tipo: {type(msg).__name__}")
        if hasattr(msg, 'content'):
            print(f"Conteúdo: {msg.content}")
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            print(f"Tool calls: {msg.tool_calls}")
        print("-" * 50)

    print("Resposta final do assistente:")
    print(result["messages"][-1].content)

if __name__ == "__main__":
    user_query = "Como posso atualizar minha fatura?"
    send_message(user_query)

    user_query = "Quero abrir um ticket para resetar minha senha"
    send_message(user_query)

    user_query = "Preciso de auxilio para instalar python no meu computador"
    send_message(user_query)