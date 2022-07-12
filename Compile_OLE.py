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
# Should not be needed due to usage of os.system()
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
    RESOURCE_PATH = os.path.join(BASE_PATH, "Resources")

else:
    # Currently does not support Linux, though the macOS UNIX exec file may suffice
    print("[COMPILE_ERROR] Linux currently not supported. Exiting...")

    sys.exit()

# Run Command to Compile OLEHandler into Executable File
print("Compiling OLEHandler into executable form...")

time.sleep(1)

# Run Command to Compile
if platform == "darwin":
    # For compiling into an .app
    # Include --windowed flag
    subprocess.run(
        [
            f"PyInstaller -F {CORE_COMPILE} -n OLEHandler --distpath {DIST_PATH} --workpath {BUILD_PATH} --windowed -y --add-data {RESOURCE_PATH}:Resources"
        ],
        shell=True
    )
    input("Completed Compilation of OLEHandler File. Press [ENTER] to finish this process...")

else:
    # For compiling in Windows
    # Due to some quirks, compilation has to occur through external shell
    print("Parsing to cmd.exe for compilation, this process will end...")
    os.system(r"start .\Win32_CompileOLE.cmd")

