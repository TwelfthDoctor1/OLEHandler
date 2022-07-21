# OLEHandler FileByte Conversion Library

# UNIX & WIN Differences
# CRLF -> \x0D\x0A, Used by Windows
# LF -> \x0A, Used by UNIX

# Byte Locator
# For 0-127 ASCII, use literal characters
# Otherwise use \x.. as stipulated in HexCode
BYTE_START_LIST = [
    b"%PDF-",
    b"\xff\xd8\xff\xe0",
    b"\x89\x50\x4e\x47",
    b"<!doctype html>"
]
BYTE_END_LIST = [
    b"%%EOF",
    b"\xff\xd9",
    b"\x49\x45\x4e\x44\xae\x42\x60\x82",
    b"</html>"
]

# Convertible FileTypes
CONVERSION_LIST = [
    "pdf",
    "jpg",
    "png",
    "html"
]
