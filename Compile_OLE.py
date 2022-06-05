import os.path
import subprocess
import sys
from pathlib import Path
import time
from sys import platform

BASE_PATH = Path(__file__).resolve().parent
CORE_COMPILE = os.path.join(BASE_PATH, "OLEHandler.py")
# print(CORE_COMPILE)

# VM Handling
if str(Path(__file__).resolve()).startswith(r"\\vmware-host"):
    print("[COMPILE NOTICE] Compilation process running in VM...")
    BASE_PATH = os.path.join("Z:", "Transfer", "GitHub", "OLEHandler")
    CORE_COMPILE = os.path.join(BASE_PATH, "OLEHandler.py")
    print(CORE_COMPILE)

# Determine Compilation Path
if platform == "win32":
    COMPILE_PATH = os.path.join(BASE_PATH, "CompileBuild", "WIN32")
    DIST_PATH = os.path.join(COMPILE_PATH, "dist")
    BUILD_PATH = os.path.join(COMPILE_PATH, "build")

elif platform == "darwin":
    COMPILE_PATH = os.path.join(BASE_PATH, "CompileBuild", "MACOS")
    DIST_PATH = os.path.join(COMPILE_PATH, "dist")
    BUILD_PATH = os.path.join(COMPILE_PATH, "build")

else:
    print("[COMPILE_ERROR] Linux currently not supported. Exiting...")

    sys.exit()

# Run Command to Compile OLEHandler into Executable File
print("Compiling OLEHandler into executable form...")
print(COMPILE_PATH)

time.sleep(1)

# Run Command to Compile
if platform == "darwin":
    subprocess.run(
        [
            f"PyInstaller -F {CORE_COMPILE} -n OLEHandler --distpath {DIST_PATH} --workpath {BUILD_PATH}"
        ],
        shell=True
    )
else:
    subprocess.run(
        [
            f"python3 -m PyInstaller -h"
        ],
        shell=True
    )
    subprocess.run(
        [
            f"python3 -m PyInstaller -F {CORE_COMPILE} -n OLEHandler --distpath {DIST_PATH} --workpath {BUILD_PATH}"
        ],
        shell=True
    )

input("Completed Compilation of OLEHandler File. Press [ENTER] to finish this process...")
