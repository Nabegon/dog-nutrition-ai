import asyncio
from agent import make_graph

async def main():
    print("LangGraph Streaming CLI")

    graph = await make_graph()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Bye!")
            break

        inputs = {"messages": [{"role": "user", "content": user_input}]}

        printed = ""

        async for event in graph.astream(inputs, stream_mode="updates"):
            for node_name in event:
                partial = event[node_name]
                msgs = partial.get("messages")
                
                last = msgs[-1]

                if getattr(last, "type", None) in ("ai", "assistant"):
                    text = last.content
                    if "</think>" in text:
                        answer_text = text.split("</think>", 1)[1].strip()
                        if "</error>" in answer_text:
                            answer_text = text.split("</error>", 1)[1].strip()
                        elif  "</answer>" in answer_text:
                            answer_text = text.split("</answer>", 1)[1].strip()
                        elif  "</response>" in answer_text:
                            answer_text = text.split("</response>", 1)[1].strip()

                    print(answer_text)
                    
if __name__ == "__main__":
    asyncio.run(main())
