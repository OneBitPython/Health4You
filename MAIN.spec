block_cipher = None


a = Analysis(['MAIN.py'],
         pathex=['C:\\Users\\anant\\PythonProjects\\Health4You'],
         binaries=[],
            datas=[
            ("C:\\Users\\anant\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\branca", "branca"),
            ("C:\\Users\\anant\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\branca\\*.json","branca"),
            ("C:\\Users\\anant\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\branca\\templates", "templates"),
            ("C:\\Users\\anant\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python39\\site-packages\\folium\\templates", "templates"),
            ],
         hiddenimports=[],
         hookspath=[],
         runtime_hooks=[],
         excludes=[],
         win_no_prefer_redirects=False,
         win_private_assemblies=False,
         cipher=block_cipher,
         noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      [],
      name='main',
      debug=False,
      bootloader_ignore_signals=False,
      strip=False,
      upx=True,
      runtime_tmpdir=None,
      console=False )
