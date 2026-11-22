"""Run from this folder: python copy_text.py"""

import shutil
from pathlib import Path

folder = Path(__file__).resolve().parent
shutil.copyfile(folder / "source.txt", folder / "destination.txt")
print("Copied source.txt to destination.txt")
