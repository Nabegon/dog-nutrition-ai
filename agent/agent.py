import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

llm = ChatOllama(model="PetrosStav/gemma3-tools:12b", base_url="http://localhost:11434")
mcp_client = MultiServerMCPClient(
    {
        "math": { "url": "http://localhost:8000/mcp", "transport": "streamable_http" }
    }
)

async def main():
    tools = await mcp_client.get_tools()
    agent = create_react_agent(llm, tools)
    response = await agent.ainvoke({"messages": "What is (3 + 5) x 12? Use a tool to calculate."})
    for message in response["messages"]:
        message.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())