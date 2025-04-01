from mcp.server.fastmcp import FastMCP, Context
from run_browser_use import run_browser_use


app = FastMCP("Browser Use")


@app.tool("Run Browser Task", "Run a task using Browse Use library inside a browser.")
async def run_browser_task(task: str, context: Context):
  """Automates a browser task using the browser-use library. Provide a natural language instruction for the task."""

  result = await run_browser_use(task, context)
  return result


if __name__ == "__main__":
  app.run("stdio")
