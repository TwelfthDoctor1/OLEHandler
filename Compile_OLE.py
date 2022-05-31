import os.path
import subprocess
from pathlib import Path
import time


CORE_COMPILE = os.path.join(Path(__file__).resolve().parent, "OLEHandler.py")
# print(CORE_COMPILE)

# Run Command to Compile OLEHandler into Executable File
print("Compiling OLEHandler into executable form...")

time.sleep(1)

subprocess.run(
    [
        f"PyInstaller -F {CORE_COMPILE} -n OLEHandler"
    ],
    shell=True
)

input("Completed Compilation of OLEHandler File. Press [ENTER] to finish this process...")
