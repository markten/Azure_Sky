import sys
from cx_Freeze import setup, Executable

setup(
    name = "GWGD_Game",
    version = "1.0",
    description = "A sample game for GWGD workshop.",
    executables = [Executable("Azure_Sky.py", base = "Win32GUI")])