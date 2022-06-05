import argparse
from OLELib.FileExtractor import convert_file
from pathlib import Path
from OLEUI import run_ui

# ======================================================================================================================
# CMD Argument Parser
parser = argparse.ArgumentParser()

# Argument Addon
parser.add_argument(
    "-x", "--extract", "-X",
    help="Extract the PPTX, DOCX or XLSX file that contains an oleObject.bin file.",
    dest="extract",
    type=Path or str
)
parser.add_argument(
    "-s", "--save", "-S",
    help="The location to save the extensions.",
    dest="saved_path",
    type=Path or str
)
parser.add_argument(
    "-d", "--debug",
    help="Start the script in DEBUG mode.",
    dest="debug",
    type=bool,
    default=False
)
parser.add_argument(
    "-ui",
    help="Run in GUI Mode.",
    dest="ui",
    type=bool,
    default=False
)

# Parse Args
cmd_args = parser.parse_args()

# Register into Core Variables
DEBUG = cmd_args.debug
FILE_PATH = cmd_args.extract
SAVED_PATH = cmd_args.saved_path
UI = cmd_args.ui

if DEBUG is True:
    print(f"[CMD ARGS]: DEBUG: {DEBUG} | {FILE_PATH} | {SAVED_PATH} | {UI}")

# ======================================================================================================================
# Run Extraction
if UI is False:
    convert_file(FILE_PATH, SAVED_PATH, DEBUG)

else:
    run_ui()

input("Press [ENTER] to continue...")
