# Dog Nutrition AI

Tool calling AI agent for dog nutrition recommendations.


## Features

- [LangGraph](https://www.langchain.com/langgraph) agent
- [FastMCP](https://gofastmcp.com/getting-started/welcome)
- Chat client (TBD)


## Installation

1. Install [Ollama](https://ollama.com/)
1. Download model: `ollama pull PetrosStav/gemma3-tools:12b`
1. Install [PDM](https://pdm-project.org)
1. Install Dependencies: `pdm install`


## Running

- Start MCP server: `pdm run mcp`
- Start agent: `pdm run agent`


## License

This project is licensed under the [MIT License](LICENSE).