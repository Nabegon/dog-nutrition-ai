import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langgraph.graph.state import CompiledStateGraph
from langchain_core.runnables.config import RunnableConfig
from langchain_ollama import ChatOllama
from agent.prompt import system_prompt

llm = ChatOllama(model="PetrosStav/gemma3-tools:12b", base_url="http://localhost:11434")
mcp_client = MultiServerMCPClient(
    {
        "math": { "url": "http://localhost:8000/mcp", "transport": "streamable_http" }
    }
)

async def make_graph(config: RunnableConfig | None = None) -> CompiledStateGraph:
    tools = await mcp_client.get_tools()
    return create_react_agent(llm, tools, prompt=system_prompt)

async def main():
    graph = await make_graph()
    response = await graph.ainvoke({"messages": "What is (3 + 5) x 12? Use a tool to calculate."})
    for message in response["messages"]:
        message.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())