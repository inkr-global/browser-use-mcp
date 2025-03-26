import asyncio
import os

from browser_use import Agent, AgentHistoryList, Browser, BrowserConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from mcp.server.fastmcp import FastMCP


googleLLM = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


mcp = FastMCP("Browser Use")


@mcp.tool()
async def run_task(task: str):
    """Run a task"""

    browser = Browser(
        config=BrowserConfig(
            chrome_instance_path=os.getenv("CHROME_PATH"),
        )
    )

    agent = Agent(
        task=task,
        llm=googleLLM,
        use_vision=True,
        browser=browser,
    )

    result = await agent.run()

    final_result = result.final_result()
    return final_result


def main():
    mcp.run()


if __name__ == "__main__":
    main()
