# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['BIBLION.py'],
             pathex=['C:\\Users\\Samuel\\Desktop\\PROYECTOS\\BIBLION\\BIBLION v1.1.1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [("./anadir_libro.py", "anadir_libro.py", "DATA"), ("./borrar_todo.py", "borrar_todo.py", "DATA"), ("./eliminar_libro.py", "eliminar_libro.py", "DATA"),("./estadisticas.py", "estadisticas.py", "DATA"),
("./Func_AnadirLibro.py", "Func_AnadirLibro.py", "DATA"),("./Func_BorrarBase.py", "Func_BorrarBase.py", "DATA"),("./Func_EliminarLibro.py", "Func_EliminarLibro.py", "DATA"),
("./Func_Estadisticas.py", "Func_Estadisticas.py", "DATA"),("./Func_VerLecturas.py", "Func_VerLecturas.py", "DATA"),("./Func_VerLibros.py", "Func_VerLibros.py", "DATA"),("./icono.ico", "icono.ico", "DATA"),("./lecturas.py", "lecturas.py", "DATA"),
("./ver_lecturas.py", "ver_lecturas.py", "DATA"),("./ver_libros.py", "ver_libros.py", "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='BIBLION',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='icono.ico')
