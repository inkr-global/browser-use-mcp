import asyncio
import os
import traceback
from datetime import datetime
from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from mcp.server.fastmcp import Context


async def run_browser_use(task: str, context: Context):
  """Run a task using Browser Use"""

  try:

    llm = ChatGoogleGenerativeAI(
      model="gemini-2.0-flash",
      api_key=os.getenv("GOOGLE_API_KEY"),
    )

    browser = Browser(
      config=BrowserConfig(
        chrome_instance_path=os.getenv("CHROME_PATH"),
        _force_keep_browser_alive=True,
      ),
    )

    context.info("Preparing new context...")

    log_folder_path_root = os.getenv("LOG_FOLDER_PATH", ".browser-use")
    session_log_folder = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_folder_path = f"{log_folder_path_root}/{session_log_folder}"

    browser_context = await browser.new_context(
      config=BrowserContextConfig(
        trace_path=f"{log_folder_path}/trace",
        save_recording_path=f"{log_folder_path}/recordings",
        save_downloads_path=f"{log_folder_path}/downloads",
      )
    )

    agent = Agent(
      task=task,
      llm=llm,
      browser=browser,
      browser_context=browser_context,
      use_vision=True,
      save_conversation_path=f"{log_folder_path}/conversations/conversation",
      generate_gif=f"{log_folder_path}/recording.gif",
    )

    try:

      context.info("Running task...")

      history = await agent.run()

      context.info("Parsing results...")

      final_result = history.final_result()
      final_result = (
        history.final_result()
        or f"No final result. Possibly incomplete. {history}"
      )
      return final_result

    except asyncio.CancelledError:
      return "Task was cancelled"

    except Exception as e:
      context.error(f"Agent run error: {str(e)}\n{traceback.format_exc()}")
      return f"Error during task execution: {str(e)}"

  except Exception as e:
    context.error(f"[run_browser_use] Error: {str(e)}\n{traceback.format_exc()}")
    return f"Error during task execution: {str(e)}"
