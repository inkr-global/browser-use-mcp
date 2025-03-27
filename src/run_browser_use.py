import os
from browser_use import Agent, Browser, BrowserConfig
from langchain_google_genai import ChatGoogleGenerativeAI


async def run_browser_use(task: str):
  """Run a task using browser use"""

  googleLLM = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

  browser = Browser(
      config=BrowserConfig(
          chrome_instance_path=os.getenv("CHROME_PATH"),
      )
  )

  agent = Agent(
      task=task,
      llm=googleLLM,
      browser=browser,
      use_vision=True,
  )

  result = await agent.run()

  final_result = result.final_result()
  return final_result
