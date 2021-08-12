import sys
from cx_Freeze import setup, Executable
exe = Executable(
    script=r"C:\Users\Samuel\Desktop\PROYECTOS\BIBLION\BIBLION v1.1\BIBLION.pyw",
    base="Win32GUI",
    )

setup(
    name = "BIBLION",
    version = "1.1",
    description = "An example",
    executables = [exe]
    )