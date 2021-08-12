import cx_Freeze
 
executables = [cx_Freeze.Executable("BIBLION.pyw",
                                 base = "Win32GUI",
                                 icon = None)]
 
build_exe_options = {"packages": [],
                     "include_files":["ventana_principal.ui"]}
 
cx_Freeze.setup(
    name = "PDF",
    version = "1.0",
    description = "",
    options={"build_exe": build_exe_options},
    executables = executables
    )
