from mcp.server.fastmcp import FastMCP, Context
from run_browser_use import run_browser_use


app = FastMCP("Browser Use")


@app.tool()
async def run_browser_task(task: str, context: Context):
  """Run a task in browser with Browser Use."""

  result = await run_browser_use(task, context)
  return result


if __name__ == "__main__":
  app.run("stdio")
