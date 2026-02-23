# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for Xalibre-zh Windows .exe

block_cipher = None

added_data = [
    ('fonts', 'Fonts'),
]

a = Analysis(
    ['Xalibre.py'],
    pathex=[],
    binaries=[],
    datas=added_data,
    hiddenimports=[
        'database',
        'converter',
        'locale_zh',
        'PIL._tkinter_finder',
        'pymupdf',
        'fitz',
        'ebooklib',
        'bs4',
        'requests',
        'pyphen',
        'pyphen.dictionaries',
        'wordfreq',
        'openai',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Xalibre',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
)
