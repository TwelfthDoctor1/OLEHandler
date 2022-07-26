from pathlib import Path
import os
import shutil
from zipfile import ZipFile
from OLELib.OLEErrorUI import OLEErrorWindow
from OLELib.OLEExtInputDialog import OLEExtInputWindow, parse_attachment
from OLELib.OLEInfoUI import OLEInfoWindow
from OLELib.FileByteInfo import BYTE_START_LIST, BYTE_END_LIST, CONVERSION_LIST

BASE_DIR = Path(__file__).resolve().parent.parent
TEMP_DIR = os.path.join(BASE_DIR, "TempFile")

# FileType Acceptance
FOLDER_NAME = ["ppt", "doc", "word", "xls"]


def convert_file(filepath: Path or str, saved_path: Path or str = "", debug=False, ui=False):
    """
    Convert the DOCX, PPTX, XLSX files into Zips and extracts them.
    :param ui: bool True/False
    :param filepath: Path or str
    :param debug: bool - True/False
    :param saved_path: Path or str
    :return:
    """
    # Init Check Filepath
    if os.path.exists(filepath) is False:
        print(f"[ERROR 0]: The specified file does not exist.")

        if ui is True:
            error_window = OLEErrorWindow(f"[ERROR 0]: The specified file does not exist.")
            error_window.show()

        return

    # Get Path of File in TempDir
    copied_dir = os.path.join(BASE_DIR, os.path.basename(filepath))

    if debug is True:
        print(f"[DEBUG]: {filepath} | {copied_dir}")

    # Copy File to TempDir
    try:
        shutil.copyfile(filepath, copied_dir)

    except shutil.Error as e:
        print(f"[ERROR 1]: File Extraction error. It is likely that the file is not a ZIP file.\n\n{e}")

        if ui is True:
            error_window = OLEErrorWindow(f"[ERROR 1]: File Extraction error. It is likely that the file "
                                          f"\nis not a ZIP file.\n\n{e}")
            error_window.show()

        return

    # Formulate ZipFile name
    # Remove existing filetype and replace with .zip
    zip_name = os.path.basename(filepath).split(".")[0] + ".zip"

    zip_path = os.path.join(BASE_DIR, zip_name)

    if debug is True:
        print(f"{copied_dir} | {zip_path}")

    # Rename File to ZipFile for Extraction
    if os.path.exists(zip_path) is False:
        os.rename(copied_dir, zip_path)

    with ZipFile(zip_path, "r") as zip_ext:
        zip_ext.extractall(TEMP_DIR)

    extract_attachments(saved_path, debug, ui)


def extract_attachments(saved_path: Path or str, debug, ui=False):
    ATTACHMENT_COUNT = 0
    PASSED_COUNT = 0
    FAILED_COUNT = 0
    EXTRACTED = False

    file_dir = None
    # Handle Undefined Saved Dir
    if saved_path == "":
        saved_path = TEMP_DIR

    for folder in FOLDER_NAME:
        if os.path.exists(os.path.join(TEMP_DIR, folder)):
            file_dir = os.path.join(TEMP_DIR, folder, "embeddings")
            break

    if file_dir is None:
        print("[ERROR 2] The Extracted file is NOT a 2007 onwards Excel/Word/Powerpoint File. (DOC, PPT and XLS are not"
              " accepted as they are from 97-2003).")

        if ui is True:
            error_window = OLEErrorWindow(
                "[ERROR 2] The Extracted file is NOT a 2007 onwards Excel/Word/Powerpoint File."
                "\n(DOC, PPT and XLS are not accepted as they are from 97-2003)."
            )
            error_window.show()

        return

    for (x, y, z) in os.walk(file_dir):
        if debug is True:
            print(f"{x} | {z}")

        ATTACHMENT_COUNT = len(z)

        for i in range(len(z)):
            # oleObject Saving Method
            if debug is True:
                print(z[i])

            if z[i].endswith("bin") and z[i].startswith("oleObject"):
                EXTRACTED = False

                if debug is True:
                    print(f"File [{z[i]}] is an oleObject.")

                # Name States
                init_sn = f"Attachment {i + 1}." + z[i].split(".")[1]
                p_init_sn = f"Attachment {i + 1}_Convert.oleconvert"
                print(f"{TEMP_DIR} | {init_sn} | {p_init_sn}")
                temp_sn = os.path.join(TEMP_DIR, init_sn)
                final_sn = os.path.join(saved_path, p_init_sn)
                # tbs = os.path.join(saved_path, z[i])

                shutil.copyfile(os.path.join(x, z[i]), temp_sn)

                with open(temp_sn, "rb") as file:
                    f_bin_data = file.read()
                    # print(f_bin_data)
                # ByteArray Conversion
                f_binarr_data = bytearray(f_bin_data)

                for byte_list_count in range(len(BYTE_START_LIST)):
                    byte_start = BYTE_START_LIST[byte_list_count]
                    byte_end = BYTE_END_LIST[byte_list_count]

                    bin_spt_1 = f_binarr_data.find(byte_start)
                    # print(bin_spt_1)

                    if bin_spt_1 != -1:
                        del f_binarr_data[:bin_spt_1]

                        bin_spt_2 = f_binarr_data.find(byte_end)

                        if bin_spt_2 == -1:
                            bin_spt_2 = len(f_binarr_data) - 1

                        fin_bin_spt_2 = len(f_binarr_data) - (bin_spt_2 + 5)

                        # print(fin_bin_spt_2)

                        del f_binarr_data[-fin_bin_spt_2]

                        if debug is True:
                            print(f"BYTE LOCATION: {bin_spt_1} | {fin_bin_spt_2}")

                        with open(final_sn, "wb") as file:
                            file.write(f_binarr_data)

                        os.remove(temp_sn)
                        PASSED_COUNT += 1

                        fin_fn = f"Attachment {i + 1}.{CONVERSION_LIST[byte_list_count]}"
                        fin_fp = os.path.join(saved_path, fin_fn)

                        # Rename the file to the current filetype
                        try:
                            os.rename(final_sn, fin_fp)

                        except Exception as e:
                            print(e)

                        if debug is True:
                            print(f"Converted Attachment {i + 1} into {fin_fp}.")

                        EXTRACTED = True

                        break

                if EXTRACTED is False:
                    if ui is True:
                        ole_input = OLEExtInputWindow(
                            ui=ui,
                            debug=debug,
                            directory=saved_path,
                            file=init_sn,
                            data=f_binarr_data
                        )
                        ole_input.show()
                    else:
                        user_ext = input("OLEHandler failed to determine filetype, please input assumed filetype: ")

                        parse_attachment(ui, debug, saved_path, init_sn, user_ext, f_binarr_data)

                    EXTRACTED = True
                    PASSED_COUNT += 1

                if EXTRACTED is False:
                    if debug is True:
                        print(f"Failed to convert Attachment {i + 1}. Skipping...")

                    os.remove(temp_sn)
                    FAILED_COUNT += 1
                    continue

            # Non oleObject Saving Method
            else:
                if debug is True:
                    print(f"File [{z[i]}] is not an oleObject.")

                # Name States
                init_sn = f"Attachment {i + 1}." + z[i].split(".")[1]
                tbs = os.path.join(saved_path, z[i])
                final_sn = os.path.join(saved_path, init_sn)

                if debug is True:
                    print(f"{saved_path} | {init_sn}")

                # User Dialog
                print(f"Saving {z[i]} as {init_sn} in {saved_path}...")

                # Save Handling
                shutil.copyfile(os.path.join(x, z[i]), tbs)
                os.rename(tbs, final_sn)

                PASSED_COUNT += 1

    print(f"[FINAL RESULT]: TOTAL -> {ATTACHMENT_COUNT} | PASSED -> {PASSED_COUNT} | FAILED -> {FAILED_COUNT}")

    if ui is True:
        ole_info = OLEInfoWindow(
            title="Extraction Status",
            text=f"Total Count: {ATTACHMENT_COUNT}\nPassed: {PASSED_COUNT}\nFailed: {FAILED_COUNT}"
        )
        ole_info.show()

    for (x, y, z) in os.walk(TEMP_DIR):
        if x == TEMP_DIR:
            for i in y:
                if os.path.exists(i):
                    os.remove(os.path.join(TEMP_DIR, i))
            for i in z:
                if os.path.exists(i):
                    os.remove(os.path.join(TEMP_DIR, i))
