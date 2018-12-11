import cx_Freeze
import sys
import matplotlib
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Network_monitor.py",
                                    base=base,
                                    icon="speedometer3.ico")]

cx_Freeze.setup(
    name = "Network_login",
    options = {"build_exe": {"packages":["tkinter","psutil"], "include_files":[
        "speedometer3.ico","C:/Users/yashr/AppData/Local/Programs/Python/Python36/DLLs/tcl86t.dll",
        "C:/Users/yashr/AppData/Local/Programs/Python/Python36/DLLs/tk86t.dll","Supportfiles"],"includes": ["tkinter"]## important
                             }},
    version = "1.0",
    description = "helps user to login into there University portal as well as tell them how much data they have used by Wi-Fi",
    executables = executables
    )
