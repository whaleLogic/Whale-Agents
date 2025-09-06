from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import AgentWorkflow

OPENAI_APIKEY="Your APIKEY here!"

def multiply(a: float, b: float) -> float:
    """Multiply two numbers and returns the product"""
    return a * b

def add(a: float, b: float) -> float:
    """Add two numbers and returns the sum"""
    return a + b

llm = OpenAI(model="gpt-4o-mini", api_key=OPENAI_APIKEY)

workflow = AgentWorkflow.from_tools_or_functions(
    [multiply, add],
    llm=llm,
    system_prompt="You are an agent that can perform basic mathematical operations using tools."
)

async def main():
    response = await workflow.run(user_msg="What is 40+(5*10)?")
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
