# Dog Nutrition AI

Tool calling AI agent for dog nutrition recommendations.


## Features

- [LangGraph](https://www.langchain.com/langgraph) agent
- [FastMCP](https://gofastmcp.com/getting-started/welcome) for tools
- [NextJS](https://nextjs.org/) chat client


## Requirements

1. [Ollama](https://ollama.com/)
1. [PDM](https://pdm-project.org)
1. Node.js (e.g. via [nvm](https://github.com/nvm-sh/nvm))


## Installation

1. Download LLM: `ollama pull PetrosStav/gemma3-tools:12b`
1. Install backend dependencies: `pdm install`
1. Install frontend dependencies: `cd frontend && npm install`
1. Create `frontend/.env` file from `frontend/.env.example`


## Running

- Start MCP server: `pdm run mcp`
- Start agent:
    - Run directly (no API): `pdm run agent`
    - Run API server (with LangGraph debug frontend): `pdm run server`
- Start frontend: `cd frontend && npm run dev`


## License

This project is licensed under the [MIT License](LICENSE).