"""
Launcher wrapper — reads PORT from the environment (set by Claude Code preview tool
when autoPort=true) and passes it to Streamlit, which doesn't read PORT itself.

Usage (direct):  python dashboard/start.py
Usage (preview): configured in .claude/launch.json
"""
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
port = os.environ.get("PORT", "8501")

subprocess.run(
    [
        sys.executable, "-m", "streamlit", "run",
        str(REPO_ROOT / "dashboard" / "app.py"),
        "--server.port", port,
        "--server.headless", "true",
        "--server.address", "localhost",
    ],
    cwd=str(REPO_ROOT),
)
