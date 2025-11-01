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
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def leseUrl(url) -> str:
    """Lese den Inhalt einer URL und gib ihn als String zurück"""
    import requests
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run(transport="streamable-http")