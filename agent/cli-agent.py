import asyncio
import sys
from langgraph_sdk import get_client
from agent import make_graph

async def main():
    print("LangGraph Streaming CLI")

    graph = await make_graph()

    while True:
        user_input = input("You: ").strip()
        print("**** user_input **** ", user_input)
        if user_input.lower() in {"exit", "quit"}:
            print("Bye!")
            break

        print("agent:", end=" ", flush=True)

        inputs = {"messages": [{"role": "user", "content": user_input}]}

        printed = ""

        async for event in graph.astream(inputs, stream_mode="updates"):
            for node_name in event:
                partial = event[node_name]
                msgs = partial.get("messages")
                
                last = msgs[-1]

                if getattr(last, "type", None) in ("ai", "assistant"):
                    // TODO rewrite
                    text = last.content
                    print("text ", text)
                    
if __name__ == "__main__":
    asyncio.run(main())
