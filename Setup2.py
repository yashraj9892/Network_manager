from cx_Freeze import *
import sys
import psutil
import signal
import threading
import time
import os
import tkinter
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Network_monitor_shortcut",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Network_monitor.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}

executables = [Executable("Network_monitor.py",
                                    base=base,
                                    icon="speedometer3.ico")]

setup(
    name = "Network login",
    options = {"build_exe": {"packages":["tkinter","psutil","os","signal","threading","time","sys"], "include_files":[
        "speedometer3.ico","C:/Users/yashr/AppData/Local/Programs/Python/Python36/DLLs/tcl86t.dll",
        "C:/Users/yashr/AppData/Local/Programs/Python/Python36/DLLs/tk86t.dll","Supportfiles"],"includes": ["tkinter"]},"bdist_msi": bdist_msi_options},
    version = "1.0",
    description = "helps user to login into there University portal as well as tell them how much data they have used by Wi-Fi",
    executables = executables
    )
