from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage


def getCommitMessageWithAI(prompt):
    llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0, max_retries=2)

    memory = [
        SystemMessage(
            content="você é um especialista em git que compara diff de arquivos e escreve mensagens apropriadas para commits, você retorna apenas a mensagem de commit em português baseado nas mudanças e com foco em commit semântico, sem nada adicional."
        ),
        HumanMessage(content=prompt),
    ]
    response = llm.invoke(memory)

    return response.content
