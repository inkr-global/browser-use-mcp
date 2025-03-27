from mcp.server.fastmcp import FastMCP
from run_browser_use import run_browser_use


app = FastMCP("Browser Use")


@app.tool()
async def run_task(task: str):
  """Run a task"""

  result = await run_browser_use(task)
  return result


if __name__ == "__main__":
  app.run()
