import os
import subprocess
import sys
from pathlib import Path
TARGET_DIR = Path(__file__).resolve().parent / "wheels"
PACKAGES = ["pandas", "openpyxl", "sqlalchemy", "psycopg2-binary"]
def download_packages():
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, "-m", "pip", "download", "--only-binary=:all:", "--platform", "win_amd64", "--python-version", "3.13", "--implementation", "cp", "--dest", str(TARGET_DIR), *PACKAGES]
    subprocess.run(cmd, check=True)
def install_packages():
    if not TARGET_DIR.exists() or not any(TARGET_DIR.glob("*.whl")):
        raise FileNotFoundError(f"Directory {TARGET_DIR} contains no wheel files.")
    cmd = [sys.executable, "-m", "pip", "install", "--no-index", "--find-links", str(TARGET_DIR), *PACKAGES]
    subprocess.run(cmd, check=True)
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "download":
        download_packages()
    else:
        install_packages()