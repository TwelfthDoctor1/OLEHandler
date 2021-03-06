![OLEHandler Banner](https://github.com/TwelfthDoctor1/OLEHandler/blob/master/GitResources/OLEHandlerBanner.png)

# OLEHandler

Extract Core Office Files (i.e. PPTX, DOCX, XLSX) and/or Convert oleObject.bin files into PDFs.

## Status

Currently **WIP**.

## Usage

To use this program, you can use the Terminal (or CMD or Powershell, etc) to run.

### UI Method

![OLEHandler UI Picture](https://github.com/TwelfthDoctor1/OLEHandler/blob/master/GitResources/OLEHandler%20UI%20Picture.png)

To decompile and extract a file, select the file to extract and the location to save the extracted attachemnts.

To start extraction, click `OK` on the dialog.

### CLI Method

To use CLI, specify the flags to run OLEHandler.

```
OLEHandler -ui "False" -x EXTRACT -s SAVED_DIR

Where:
EXTRACT -> Path of File to be extracted
SAVED_DIR -> Path of Directory to save the Attachments

Note:
For Paths on UNIX, to specify a space, do "\ ". E.g. /Volumes/Transfer/Some\ File/
```

By default, just executing the file should open up the GUI.

To use CLI, follow the command above to use it.

## Compiling

Required Modules (Modules not required in Python):
* PyQt5
* PyQt5-tools (Only needed if altering UI, requires Python 3.9 or lower)
* PyInstaller

As the compilation method makes use of the specified installed Python Version (not the VirtualEnv, I think) you should also install the modules on that version using pip besides installing on the VirtualEnv.

To compile, run Compile_OLE.py. For macOS, the python file will run a command to compile. As for Windows, compilation occurs through a Batch Command File.
