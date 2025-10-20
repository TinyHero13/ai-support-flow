from langchain.tools import tool

@tool("faq_tool")
def faq_node(query: str) -> str:
    """
    Use esta ferramenta sempre que o usuário fizer uma pergunta sobre:
    - Atualizar fatura ou boleto
    - Cancelar assinatura
    - Informações sobre suporte
    
    Esta ferramenta contém respostas oficiais do FAQ.
    """
    faqs = {
        "atualizar minha fatura": "Você pode atualizar sua fatura acessando o portal do cliente e clicando em 'Reemitir boleto'.",
        "cancelar": "Para cancelar sua assinatura, vá em Configurações > Assinaturas > Cancelar.",
        "suporte": "Nosso suporte funciona de segunda a sexta, das 8h às 18h."
    }

    query_lower = query.lower()
    for key, answer in faqs.items():
        if key in query_lower:
            return answer
    return "Desculpe, não encontrei uma resposta para sua pergunta. Deseja abrir um ticket?"
