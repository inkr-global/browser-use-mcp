import asyncio
import sys
from run_browser_use import run_browser_use


if __name__ == "__main__":
  task = " ".join(sys.argv[1:])
  asyncio.run(run_browser_use(task))
