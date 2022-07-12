python3 -m PyInstaller -F ".\OLEHandler.py" -n "OLEHandler" --distpath ".\CompileBuild\WIN32\dist" --workpath ".\CompileBuild\WIN32\build" --nowindowed -y --add-data ".\Resources";Resources

exit