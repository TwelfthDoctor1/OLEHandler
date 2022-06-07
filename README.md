# OLEHandler

Extract Core Office Files (i.e. PPTX, DOCX, XLSX) and/or Convert oleObject.bin files.

### Status

Currently **WIP**.

### Usage

To use this program, you can use the Terminal (or CMD or Powershell, etc) to run.

Specify the flags to run OLEHandler.

```
OLEHandler -ui "False" -x EXTRACT -s SAVED_DIR

Where:
EXTRACT -> Path of File to be extracted
SAVED_DIR -> Path of Directory to save the Attachments

Note:
For Paths on UNIX, to specify a space, do "\ ". E.g. /Volumes/Transfer/Some\ File/
```

**UI based method is still being implemented. Currently, the file will error out on launch. CLI Method only applicable.**

By default, just executing the file should open up the GUI.