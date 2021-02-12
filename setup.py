from cx_Freeze import setup, Executable
setup(name='instrumentsettings', version='1.2', description='Dumps M8070 parameters from preset', executables = [Executable("instrumentsettingsmain.py")])