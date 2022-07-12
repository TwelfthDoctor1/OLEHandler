# OLEHandler

Extract Core Office Files (i.e. PPTX, DOCX, XLSX) and/or Convert oleObject.bin files into PDFs.

### Status

Currently **WIP**.

### Usage

To use this program, you can use the Terminal (or CMD or Powershell, etc) to run.

# UI Method

![OLEHandler UI Picture](https://github.com/TwelfthDoctor1/OLEHandler/blob/main/GitResources/OLEHandler%20UI%20Picture.png)

# CLI Method

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