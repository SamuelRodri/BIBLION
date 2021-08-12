import cx_Freeze
import sys

if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
executables = [cx_Freeze.Executable("BIBLION.py",
                                    base = "Win32GUI",
                                    icon = "icono.ico",
                                    )]

build_exe_options = {"packages": None,
                    "include_files":"icono.png"}


cx_Freeze.setup(
    name = "",
    version = "",
    description = "",
    options = {"build_exe": build_exe_options},
    executables = executables
    )