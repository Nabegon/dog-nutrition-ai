from mcp.server.fastmcp import FastMCP
from langchain_community.tools import DuckDuckGoSearchRun

mcp = FastMCP("Math")

@mcp.tool()
def search(query: str) -> str:
    """Perform a web search and return the results."""
    search_tool = DuckDuckGoSearchRun()
    results = search_tool.run(query)
    return results

@mcp.tool()
def readUrl(url) -> str:
    """Read the content of a URL and return it as a string"""
    import requests
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="streamable-http")
